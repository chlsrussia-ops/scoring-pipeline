from __future__ import annotations
from contracts import ScoreRequest, ScoreResult
from scoring_engine import compute_breakdown
from caps import apply_caps
from fallback import fallback_result
from diagnostics import collect_diagnostics, get_logger
from analytics import track
from observability import emit_event, emit_metric

def execute(request: ScoreRequest) -> ScoreResult:
    logger = get_logger()
    try:
        request.validate()
        breakdown = compute_breakdown(request)
        cap_result = apply_caps(breakdown.base_score)
        diagnostics = collect_diagnostics(f"items={breakdown.item_count}", f"numeric_sum={breakdown.numeric_sum}", f"capped={cap_result.capped}")
        result = ScoreResult(ok=True, final_score=cap_result.value, capped=cap_result.capped, used_fallback=False, reason=None, breakdown=breakdown, request_id=request.request_id, diagnostics=diagnostics)
        track("score_executed", request_id=request.request_id)
        emit_metric("score.final", result.final_score, request_id=request.request_id)
        return result
    except Exception as exc:
        logger.exception("execution failed request_id=%s", getattr(request, "request_id", "unknown"))
        safe_request = request if isinstance(request, ScoreRequest) else ScoreRequest(payload={}, request_id="unknown", source="unknown")
        result = fallback_result(safe_request, reason=str(exc))
        track("score_fallback", request_id=result.request_id)
        return result
