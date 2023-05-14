from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class onConnectRequest(_message.Message):
    __slots__ = ["instance_name", "ip_address"]
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    ip_address: str
    def __init__(self, ip_address: _Optional[str] = ..., instance_name: _Optional[str] = ...) -> None: ...

class onConnectResponse(_message.Message):
    __slots__ = ["is_accepted"]
    IS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    is_accepted: bool
    def __init__(self, is_accepted: bool = ...) -> None: ...
