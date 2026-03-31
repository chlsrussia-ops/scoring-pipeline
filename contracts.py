from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Mapping

class ValidationError(ValueError):
    pass

@dataclass(slots=True, frozen=True)
class ScoreRequest:
    payload: dict[str, Any]
    request_id: str = "unknown"
    source: str = "local"
    def validate(self) -> None:
        if not isinstance(self.payload, dict):
            raise ValidationError("payload must be a dict")
        if not self.request_id or not isinstance(self.request_id, str):
            raise ValidationError("request_id must be a non-empty string")
        if not self.source or not isinstance(self.source, str):
            raise ValidationError("source must be a non-empty string")

@dataclass(slots=True, frozen=True)
class ScoreBreakdown:
    base_score: float
    item_count: int
    numeric_sum: float
    text_weight: float
    bonuses: Mapping[str, float] = field(default_factory=dict)

@dataclass(slots=True, frozen=True)
class ScoreResult:
    ok: bool
    final_score: float
    capped: bool
    used_fallback: bool
    reason: str | None
    breakdown: ScoreBreakdown
    request_id: str
    diagnostics: tuple[str, ...] = ()
    def to_dict(self) -> dict[str, Any]:
        return {"ok": self.ok, "final_score": self.final_score, "capped": self.capped, "used_fallback": self.used_fallback, "reason": self.reason, "breakdown": {"base_score": self.breakdown.base_score, "item_count": self.breakdown.item_count, "numeric_sum": self.breakdown.numeric_sum, "text_weight": self.breakdown.text_weight, "bonuses": dict(self.breakdown.bonuses)}, "request_id": self.request_id, "diagnostics": list(self.diagnostics)}
