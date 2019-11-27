Generate Proto Files

```bash
python3 -m grpc_tools.protoc --proto_path=../../protobuf-definitions/ --python_out=. --grpc_python_out=. ../../protobuf-definitions/services/simulator.proto
```

Note: we need `set DISPLAY=:0` and XMING on windows

## Info

Multi Dimensional array over Protobuf

arr = np.array([ [ [ 0, 1, 2 ], [ 3, 4, 5 ] ], [ [ 6, 7, 8 ], [ 9, 10, 11 ] ] ]) # Create (2, 2, 3) array
print(arr)
flatten = arr.flatten()
print("Flatten")
print(flatten)
print("Unflatten")
print(flatten.reshape((2, 2, 3)))

## Running Tests

```bash
pip3 install -U pytest
pytest test-spaces.py
```
