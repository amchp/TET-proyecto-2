#Replication.proto
python3 -m grpc_tools.protoc -I .  --python_out=../generated/connection/  --pyi_out=../generated/connection/ --grpc_python_out=../generated/connection/ Connection.proto
#Update.proto
python3 -m grpc_tools.protoc -I .  --python_out=../generated/heartbeat/  --pyi_out=../generated/heartbeat/ --grpc_python_out=../generated/heartbeat/ Heartbeat.proto