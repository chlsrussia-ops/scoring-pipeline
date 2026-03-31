from __future__ import annotations
import logging
from typing import Iterable

def configure_logging(level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger("score_pipeline")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s"))
        logger.addHandler(handler)
    logger.setLevel(level); logger.propagate = False
    return logger

def get_logger() -> logging.Logger:
    return configure_logging()

def collect_diagnostics(*messages: str) -> tuple[str, ...]:
    return tuple(msg for msg in messages if msg)
