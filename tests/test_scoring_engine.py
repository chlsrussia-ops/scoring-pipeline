from contracts import ScoreRequest
from scoring_engine import compute_breakdown

def test_breakdown_shape():
    r = compute_breakdown(ScoreRequest(payload={"a": 10, "b": 20.5, "text": "hello", "tags": [1,2,3], "meta": {"x": 1}, "flag": True}, request_id="r1", source="test"))
    assert r.item_count == 6
    assert r.numeric_sum >= 30.5
    assert r.base_score > 0
