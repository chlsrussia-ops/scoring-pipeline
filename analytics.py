from __future__ import annotations
from collections import Counter
from dataclasses import dataclass, field
from typing import Any

@dataclass
class AnalyticsCollector:
    counters: Counter = field(default_factory=Counter)
    def track(self, event: str, **dimensions: Any) -> None:
        self.counters[event] += 1
    def snapshot(self) -> dict[str, int]:
        return dict(self.counters)

collector = AnalyticsCollector()
def track(event: str, **dimensions: Any) -> None:
    collector.track(event, **dimensions)
