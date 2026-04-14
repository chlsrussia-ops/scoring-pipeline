# scoring-pipeline

## Назначение
Пайплайн скоринга с контрактами, capping-логикой, fallback-стратегиями
и reviewer-этапом. Считает оценки для downstream-решений.

## Стек
- Python, FastAPI
- shared-contracts (Pydantic)
- pytest

## Место в экосистеме
Scoring-слой между данными и decision-engine. Полная картина:
[chlsrussia-ops/content-factory-v4 → docs/ARCHITECTURE_MAP.md](https://github.com/chlsrussia-ops/content-factory-v4/blob/main/docs/ARCHITECTURE_MAP.md)

## Запуск
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Статус
Активный.
