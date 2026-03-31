from contracts import ScoreBreakdown, ScoreResult
from reviewer import review

def _r(score, ok=True):
    return ScoreResult(ok=ok, final_score=score, capped=False, used_fallback=not ok, reason=None if ok else "f", breakdown=ScoreBreakdown(base_score=score, item_count=1, numeric_sum=0, text_weight=0), request_id="r1")

def test_approved(): assert review(_r(55)).approved
def test_manual(): assert review(_r(25)).label == "manual_review"
def test_rejected_not_ok(): assert review(_r(0, ok=False)).label == "rejected"
