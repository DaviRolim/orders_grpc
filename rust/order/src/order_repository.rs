use crate::order::{OrderId, OrderRequest};
use rusqlite::{params, Connection, Result};

// pub fn test_returns() -> Result<(), rusqlite::Error> {
//     Ok(());
// }

pub fn delete_order(order_id: &OrderId) -> Result<(), rusqlite::Error> {
    let path = "./my_db.db3";
    let conn = Connection::open(path).unwrap();
    println!("OrderId {}", order_id.id);
    match conn.execute(
        "DELETE FROM orers where orders.id = ?1",
        params![order_id.id],
    ) {
        Ok(_) => return Ok(()),
        Err(e) => return Err(e),
    };
}

pub fn save_order(order: &OrderRequest) {
    let path = "./my_db.db3";
    let conn = Connection::open(path).unwrap();
    conn.execute(
        "INSERT INTO orders (id, name, price, quantity) VALUES (?1, ?2, ?3, ?4)",
        (&order.id, &order.name, &order.price, &order.quantity),
    )
    .unwrap();
}
pub fn update_order(order: &OrderRequest) {
    let path = "./my_db.db3";
    let conn = Connection::open(path).unwrap();
    conn.execute(
        "UPDATE orders set  name = ?1, price = ?2, quantity = ?3 WHERE id = ?4",
        (&order.name, &order.price, &order.quantity, &order.id),
    )
    .unwrap();
}

pub fn list_orders() -> Result<Vec<OrderRequest>, Box<dyn std::error::Error>> {
    let path = "./my_db.db3";
    let conn = Connection::open(path).unwrap();
    let mut stmt = conn
        .prepare("SELECT id, name, price, quantity FROM orders")
        .unwrap();
    let order_iter = stmt
        .query_map([], |row| {
            Ok(OrderRequest {
                id: row.get(0)?,
                name: row.get(1)?,
                price: row.get(2)?,
                quantity: row.get(3)?,
            })
        })
        .unwrap();
    let mut orders = vec![];
    for order in order_iter {
        let order = order.unwrap();
        println!("Found order {:?}", &order);
        orders.push(order);
    }
    Ok(orders)
}
