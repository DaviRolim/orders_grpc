use rusqlite::{Connection, Result};
use tonic::{transport::Server, Code, Request, Response, Status};

use order::order_server::{Order, OrderServer};
use order::{OrderReply, OrderRequest};
use tokio::sync::mpsc;
use tokio_stream::wrappers::ReceiverStream;

pub mod order {
    tonic::include_proto!("order"); // The string specified here must match the proto package name
}

mod order_repository;

#[derive(Debug, Default)]
pub struct MyOrder {}

#[tonic::async_trait]
impl Order for MyOrder {
    type ListOrderStream = ReceiverStream<Result<OrderRequest, Status>>;

    async fn update_order(
        &self,
        request: Request<order::OrderRequest>,
    ) -> Result<Response<OrderReply>, Status> {
        let req = request.into_inner();
        println!("Got a request: {:?}", req);
        order_repository::update_order(&req);
        let reply = order::OrderReply {
            status: 201,
            message: format!("Updated item {}!", &req.name),
        };

        Ok(Response::new(reply))
    }
    async fn delete_order(
        &self,
        request: Request<order::OrderId>,
    ) -> Result<Response<OrderReply>, Status> {
        if order_repository::delete_order(&request.into_inner()).is_err() {
            return Err(Status::new(Code::Internal, "Deu errado!"));
        };
        let reply = order::OrderReply {
            status: 200,
            message: "Item deleted successfully".to_string(),
        };
        Ok(Response::new(reply))
    }

    async fn list_order(
        &self,
        _request: Request<order::Empty>,
    ) -> Result<Response<Self::ListOrderStream>, Status> {
        let orders = order_repository::list_orders().unwrap();
        let (tx, rx) = mpsc::channel(4);
        tokio::spawn(async move {
            for order in &orders[..] {
                tx.send(Ok(order.clone())).await.unwrap();
            }
        });
        Ok(Response::new(Self::ListOrderStream::new(rx)))
    }

    async fn send_order(
        &self,
        request: Request<OrderRequest>,
    ) -> Result<Response<OrderReply>, Status> {
        let req = request.into_inner();
        println!("Got a request: {:?}", req);
        order_repository::save_order(&req);
        // order_repository::list_orders();
        let reply = order::OrderReply {
            status: 201,
            message: format!("Saved item {}!", &req.name),
        };

        Ok(Response::new(reply))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::]:50051".parse()?;
    let order = MyOrder::default();
    let path = "./my_db.db3";
    let conn = Connection::open(path)?;

    conn.execute(
        "CREATE TABLE if not exists orders (
            id   TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )",
        (), // empty list of parameters.
    )?;

    Server::builder()
        .add_service(OrderServer::new(order))
        .serve(addr)
        .await?;

    Ok(())
}
