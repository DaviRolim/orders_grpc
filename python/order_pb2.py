# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0border.proto\x12\x05order\"\x07\n\x05\x45mpty\"\x15\n\x07OrderId\x12\n\n\x02id\x18\x01 \x01(\t\"I\n\x0cOrderRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\x10\n\x08quantity\x18\x04 \x01(\x05\"-\n\nOrderReply\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t2\xdf\x01\n\x05Order\x12\x35\n\tSendOrder\x12\x13.order.OrderRequest\x1a\x11.order.OrderReply\"\x00\x12\x32\n\tListOrder\x12\x0c.order.Empty\x1a\x13.order.OrderRequest\"\x00\x30\x01\x12\x32\n\x0b\x44\x65leteOrder\x12\x0e.order.OrderId\x1a\x11.order.OrderReply\"\x00\x12\x37\n\x0bUpdateOrder\x12\x13.order.OrderRequest\x1a\x11.order.OrderReply\"\x00\x62\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_ORDERID = DESCRIPTOR.message_types_by_name['OrderId']
_ORDERREQUEST = DESCRIPTOR.message_types_by_name['OrderRequest']
_ORDERREPLY = DESCRIPTOR.message_types_by_name['OrderReply']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.Empty)
  })
_sym_db.RegisterMessage(Empty)

OrderId = _reflection.GeneratedProtocolMessageType('OrderId', (_message.Message,), {
  'DESCRIPTOR' : _ORDERID,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.OrderId)
  })
_sym_db.RegisterMessage(OrderId)

OrderRequest = _reflection.GeneratedProtocolMessageType('OrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERREQUEST,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.OrderRequest)
  })
_sym_db.RegisterMessage(OrderRequest)

OrderReply = _reflection.GeneratedProtocolMessageType('OrderReply', (_message.Message,), {
  'DESCRIPTOR' : _ORDERREPLY,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.OrderReply)
  })
_sym_db.RegisterMessage(OrderReply)

_ORDER = DESCRIPTOR.services_by_name['Order']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=22
  _EMPTY._serialized_end=29
  _ORDERID._serialized_start=31
  _ORDERID._serialized_end=52
  _ORDERREQUEST._serialized_start=54
  _ORDERREQUEST._serialized_end=127
  _ORDERREPLY._serialized_start=129
  _ORDERREPLY._serialized_end=174
  _ORDER._serialized_start=177
  _ORDER._serialized_end=400
# @@protoc_insertion_point(module_scope)
