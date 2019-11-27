import numpy as np
import services.simulator_pb2 as simulator_pb2

def serialize(obj):
    className = obj.__class__.__name__

    res = simulator_pb2.MetaSpaceWrapper()

    if className == 'Box':
        res.box.CopyFrom(serializeBox(obj))
    elif className == 'Discrete':
        res.discrete.CopyFrom(serializeDiscrete(obj))
    elif className == 'Tuple':
        res.tuple.CopyFrom(serializeTuple(obj))

    return res

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