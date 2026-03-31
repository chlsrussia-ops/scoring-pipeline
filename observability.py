from __future__ import annotations
from typing import Any

def emit_metric(name: str, value: float, **tags: Any) -> None:
    pass  # production: send to metrics backend

def emit_event(name: str, **payload: Any) -> None:
    pass  # production: send to event bus
