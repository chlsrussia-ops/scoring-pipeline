from __future__ import annotations
import sys
from contracts import ScoreRequest
from executor import execute
from serializer import serialize

def main() -> int:
    payload = {"a": 10, "b": 5.5, "comment": "hello", "tags": ["x", "y"], "meta": {"k": 1}}
    request = ScoreRequest(payload=payload, request_id="demo", source="cli")
    result = execute(request)
    print(serialize(result.to_dict(), indent=2))
    return 0 if result.ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
