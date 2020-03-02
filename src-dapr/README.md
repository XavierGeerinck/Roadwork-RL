# README

## Compiling Protobuf

```bash
# 1. Compiling Roadwork Protobuf
python -m grpc_tools.protoc --proto_path=../proto/roadwork/ --python_out=proto_compiled/ --grpc_python_out=proto_compiled/ ../proto/roadwork/roadwork.proto

# 2. Compiling Dapr
python -m grpc_tools.protoc --proto_path=../proto/dapr/ --python_out=proto_compiled/ --grpc_python_out=proto_compiled/ ../proto/dapr/dapr.proto
python -m grpc_tools.protoc --proto_path=../proto/dapr/ --python_out=proto_compiled/ --grpc_python_out=proto_compiled/ ../proto/dapr/daprclient.proto
```