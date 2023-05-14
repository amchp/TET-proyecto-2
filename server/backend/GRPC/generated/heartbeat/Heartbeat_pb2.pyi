from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HeartbeatResponse(_message.Message):
    __slots__ = ["load"]
    LOAD_FIELD_NUMBER: _ClassVar[int]
    load: float
    def __init__(self, load: _Optional[float] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
