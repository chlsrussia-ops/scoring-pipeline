from __future__ import annotations
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class CapResult:
    value: float; capped: bool; cap_limit: float

def apply_caps(value: float, *, min_value: float = 0.0, max_value: float = 100.0) -> CapResult:
    normalized = max(min_value, min(value, max_value))
    return CapResult(value=round(normalized, 4), capped=(normalized != value), cap_limit=max_value)
