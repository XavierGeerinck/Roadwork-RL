from gym.spaces import Tuple, Box, Discrete, MultiDiscrete, MultiBinary

import services.simulator_pb2 as simulator_pb2
import services.simulator_pb2_grpc as simulator_pb2_grpc

import numpy as np

def test_serialize_box():
    obj = Box(low=-1, high=2, shape=(3, 4))
    serialized = serialize(obj)

    sizeFlattened = 3 * 4

    assert serialized.dimensions == [3, 4]
    assert len(serialized.dimensionDouble.low) == sizeFlattened
    assert serialized.dimensionDouble.low == [ -1.0 ] * sizeFlattened
    assert len(serialized.dimensionDouble.high) == sizeFlattened
    assert serialized.dimensionDouble.high == [ 2.0 ] * sizeFlattened

# @todo: this tests for RGB image serialization, to include an int type check (now it's a double)
def test_serialize_box_2():
    obj = Box(low=0, high=255, shape=(8, 8, 3)) # 8 x 8 RGB picture
    serialized = serialize(obj)

    sizeFlattened = 8 * 8 * 3

    assert serialized.dimensions == [8, 8, 3]
    assert len(serialized.dimensionDouble.low) == sizeFlattened
    assert serialized.dimensionDouble.low == [ 0 ] * sizeFlattened
    assert len(serialized.dimensionDouble.high) == sizeFlattened
    assert serialized.dimensionDouble.high == [ 255 ] * sizeFlattened

def test_serialize_box_3():
    obj = Box(np.array([ -1, 0, 0 ]), np.array([ +1, +1, +1 ]))
    serialized = serialize(obj)

    sizeFlattened = 1 * 3

    assert serialized.dimensions == [ 3 ]
    assert len(serialized.dimensionDouble.low) == sizeFlattened
    assert serialized.dimensionDouble.low == [ -1.0, 0.0, 0.0 ]
    assert len(serialized.dimensionDouble.high) == sizeFlattened
    assert serialized.dimensionDouble.high == [ 1.0, 1.0, 1.0 ]

def test_serialize_box_4():
    obj = Box(low=-1, high=2, shape=(1, 4))
    serialized = serialize(obj)

    sizeFlattened = 1 * 4

    assert serialized.dimensions == [4]
    assert len(serialized.dimensionDouble.low) == sizeFlattened
    assert serialized.dimensionDouble.low == [ -1.0 ] * sizeFlattened
    assert len(serialized.dimensionDouble.high) == sizeFlattened
    assert serialized.dimensionDouble.high == [ 2.0 ] * sizeFlattened

def test_serialize_discrete():
    obj = Discrete(5)
    serialized = serialize(obj)

    assert serialized.n == 5

def test_serialize_tuple():
    d1 = Discrete(5)
    d2 = Discrete(3)
    d3 = Discrete(1)

    obj = Tuple([ d1, d2, d3 ])
    serialized = serialize(obj)

    assert len(serialized.spaces) == 3
    assert serialized.spaces[0].discrete.n == d1.n
    assert serialized.spaces[1].discrete.n == d2.n
    assert serialized.spaces[2].discrete.n == d3.n

def test_serialize_tuple_2():
    d1 = Discrete(5)
    b2 = Box(0, 255, shape=(2, 2, 3)) # 2x2 px RGB picture
    d3 = Discrete(1)

    obj = Tuple([ d1, b2, d3 ])
    serialized = serialize(obj)

    assert len(serialized.spaces) == 3
    assert serialized.spaces[0].discrete.n == d1.n
    assert serialized.spaces[1].box.dimensionDouble.low == b2.low.flatten().tolist()
    assert serialized.spaces[1].box.dimensionDouble.high == b2.high.flatten().tolist()
    assert serialized.spaces[1].box.dimensions == np.asarray(b2.shape).tolist()
    assert serialized.spaces[2].discrete.n == d3.n

def test_serialize_tuple_3():
    d1 = Discrete(5)
    b2 = Box(0, 255, shape=(2, 2, 3)) # 2x2 px RGB picture
    d3 = Discrete(1)

    obj = Tuple([ Tuple([ d1, b2 ]), d3 ])
    serialized = serialize(obj)

    assert len(serialized.spaces) == 2
    assert serialized.spaces[0].tuple.spaces[0].discrete.n == d1.n
    assert serialized.spaces[0].tuple.spaces[1].box.dimensionDouble.low == b2.low.flatten().tolist()
    assert serialized.spaces[0].tuple.spaces[1].box.dimensionDouble.high == b2.high.flatten().tolist()
    assert serialized.spaces[0].tuple.spaces[1].box.dimensions == np.asarray(b2.shape).tolist()
    assert serialized.spaces[1].discrete.n == d3.n

def test_serialize_tuple_4():
    d1 = Discrete(5)
    b2 = Box(0, 255, shape=(2, 2, 3)) # 2x2 px RGB picture
    d3 = Discrete(1)
    d4 = Discrete(255)

    obj = Tuple([ Tuple([ d1, Tuple([ b2, d3 ]) ]), d4 ])
    serialized = serialize(obj)

    assert len(serialized.spaces) == 2
    assert serialized.spaces[0].tuple.spaces[0].discrete.n == d1.n
    assert serialized.spaces[0].tuple.spaces[1].tuple.spaces[0].box.dimensionDouble.low == b2.low.flatten().tolist()
    assert serialized.spaces[0].tuple.spaces[1].tuple.spaces[0].box.dimensionDouble.high == b2.high.flatten().tolist()
    assert serialized.spaces[0].tuple.spaces[1].tuple.spaces[0].box.dimensions == np.asarray(b2.shape).tolist()
    assert serialized.spaces[0].tuple.spaces[1].tuple.spaces[1].discrete.n == d3.n
    assert serialized.spaces[1].discrete.n == d4.n

    print(serialize(Tuple([ Box(0, 255, shape=(64, 64, 3)), Box(-50, 50, shape=(3, )) ])))
    assert 1 == 2

def serialize(obj):
    className = obj.__class__.__name__

    if className == 'Box':
        obj = serializeBox(obj)
    elif className == 'Discrete':
        obj = serializeDiscrete(obj)
    elif className == 'Tuple':
        obj = serializeTuple(obj)

    return obj

def unserialize(obj):
    return ""

# https://github.com/openai/gym/blob/master/gym/spaces/box.py
def serializeBox(b):
    result = simulator_pb2.MetaSpaceBox()

    if b.shape[0] == 1:
        result.dimensions.extend(np.asarray(b.shape[1:]).tolist())
    else:
        result.dimensions.extend(np.asarray(b.shape).tolist())

    result.dimensionDouble.low.extend(b.low.flatten().tolist())
    result.dimensionDouble.high.extend(b.high.flatten().tolist())
    
    return result

def serializeDiscrete(d):
    result = simulator_pb2.MetaSpaceDiscrete()
    result.n = d.n

    return result

# https://github.com/openai/gym/blob/master/gym/spaces/tuple.py
def serializeTuple(t):
    result = simulator_pb2.MetaSpaceTuple()

    for t in t.spaces:
        tCN = t.__class__.__name__
        serializedTupleValue = serialize(t)
        serializedTupleValueCN = serializedTupleValue.__class__.__name__

        resultWrapper = simulator_pb2.MetaSpaceWrapper()

        if serializedTupleValueCN == 'MetaSpaceDiscrete':
            # resultWrapper.discrete.n = serializedTupleValue.n
            resultWrapper.discrete.CopyFrom(serializedTupleValue)
        elif serializedTupleValueCN == 'MetaSpaceBox':
            resultWrapper.box.CopyFrom(serializedTupleValue)
        elif serializedTupleValueCN == 'MetaSpaceTuple':
            resultWrapper.tuple.CopyFrom(serializedTupleValue)

        result.spaces.extend([ resultWrapper ])

    return result