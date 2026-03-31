from serializer import serialize, deserialize

def test_roundtrip():
    data = {"a": 1, "b": "text"}
    assert deserialize(serialize(data)) == data
