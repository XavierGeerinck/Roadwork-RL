# Protobuf

Protobuf is being used to serialize a state in a compact way, so it can be transferred over a medium to be used by another language. Allowing us to interact with simulators in a bi-directional way from any language that implements these Protocol buffers.

## Building the Protobuf language SDKs

Protobuf has a tool called `protoc` that allows you to convert `.proto` files towards the source files for the respective langauges. For [grpc.io](https://grpc.io/) we will have to build the Protobuf files as part of the GRPC bindings. For this we will need `python -m pip install grpcio-tools` to be installed, whereafter we can run the following:

```bash
echo "[SDK][Python] Building GRPC Protobuf Bindings"
mkdir -p src/SDKS/python/grpc_compiled
python -m grpc_tools.protoc -Isrc/protobuf-definitions/ --python_out=src/SDKs/python/grpc_compiled --grpc_python_out=src/SDKs/python/grpc_compiled --proto_path=src/protobuf-definitions/ src/protobuf-definitions/{,**/}*/*.proto
echo -e "import sys\nfrom pathlib import Path\nsys.path.append(str(Path(__file__).parent))" > src/SDKs/python/grpc_compiled/__init__.py

echo "[SimulatorIntegration][Python] Building GRPC Protobuf Bindings"
mkdir -p src/SimulatorIntegrations/OpenAI-Gym/grpc_compiled
python -m grpc_tools.protoc -Isrc/protobuf-definitions/ --python_out=src/SimulatorIntegrations/OpenAI-Gym/grpc_compiled --grpc_python_out=src/SimulatorIntegrations/OpenAI-Gym/grpc_compiled --proto_path=src/protobuf-definitions/ src/protobuf-definitions/{,**/}*/*.proto
echo -e "import sys\nfrom pathlib import Path\nsys.path.append(str(Path(__file__).parent))" > src/SimulatorIntegrations/OpenAI-Gym/grpc_compiled/__init__.py
```

python3 -m grpc_tools.protoc --proto_path=../../protobuf-definitions/ --python_out=. --grpc_python_out=. ../../protobuf-definitions/services/simulator.proto
