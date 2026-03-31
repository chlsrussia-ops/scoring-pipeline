from contracts import ScoreRequest
from executor import execute

def test_success():
    r = execute(ScoreRequest(payload={"a": 10, "b": "hello"}, request_id="e1", source="test"))
    assert r.ok and not r.used_fallback and r.final_score >= 0

def test_fallback():
    r = execute(ScoreRequest(payload="wrong", request_id="e2", source="test"))
    assert not r.ok and r.used_fallback and r.final_score == 0.0
