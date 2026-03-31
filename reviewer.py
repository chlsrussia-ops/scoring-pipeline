from __future__ import annotations
from dataclasses import dataclass
from contracts import ScoreResult

@dataclass(slots=True, frozen=True)
class ReviewDecision:
    approved: bool; label: str; reason: str

def review(result: ScoreResult) -> ReviewDecision:
    if not result.ok: return ReviewDecision(False, "rejected", "result is not ok")
    if result.final_score >= 80: return ReviewDecision(True, "excellent", "score is very strong")
    if result.final_score >= 50: return ReviewDecision(True, "approved", "score passed threshold")
    if result.final_score >= 20: return ReviewDecision(False, "manual_review", "needs manual inspection")
    return ReviewDecision(False, "rejected", "score below acceptable threshold")
