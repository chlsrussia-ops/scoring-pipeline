from __future__ import annotations
from typing import Any
from contracts import ScoreBreakdown, ScoreRequest

def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)

def compute_breakdown(request: ScoreRequest) -> ScoreBreakdown:
    payload = request.payload
    item_count = len(payload)
    numeric_sum = 0.0; text_weight = 0.0; bonuses: dict[str, float] = {}
    for key, value in payload.items():
        if _is_number(value): numeric_sum += float(value)
        elif isinstance(value, str): text_weight += min(len(value) * 0.25, 10.0)
        elif isinstance(value, (list, tuple, set)): bonuses[f"{key}_collection_bonus"] = min(len(value) * 0.75, 8.0)
        elif isinstance(value, dict): bonuses[f"{key}_nested_bonus"] = min(len(value) * 1.5, 12.0)
        elif value is True: bonuses[f"{key}_flag_bonus"] = 2.0
    base_score = item_count * 2.0 + numeric_sum * 0.1 + text_weight + sum(bonuses.values())
    return ScoreBreakdown(base_score=round(base_score, 4), item_count=item_count, numeric_sum=round(numeric_sum, 4), text_weight=round(text_weight, 4), bonuses=bonuses)
