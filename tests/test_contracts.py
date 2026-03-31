import pytest
from contracts import ScoreRequest, ValidationError

def test_validation_success():
    ScoreRequest(payload={"a": 1}, request_id="r1", source="test").validate()

def test_validation_fails_non_dict():
    with pytest.raises(ValidationError):
        ScoreRequest(payload="bad", request_id="r1", source="test").validate()
