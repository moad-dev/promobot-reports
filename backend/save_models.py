from transformers import pipeline

MODELS_PATH="ai_models/"

MODELS = [
    "nizamovtimur/rubert-base-cased-reports-group-topic-classification",
    "nizamovtimur/rubert-tiny-reports-landscaping-classification",
    "nizamovtimur/rubert-tiny-reports-transport-classification",
    "nizamovtimur/rubert-tiny-reports-garbage-classification",
    "nizamovtimur/rubert-tiny-reports-zhkh-classification",
    "nizamovtimur/rubert-tiny-reports-covid-classification",
    "nizamovtimur/rubert-tiny-reports-social-service-classification",
    "nizamovtimur/rubert-tiny-reports-health-classification",
    "nizamovtimur/rubert-tiny-reports-education-classification",
    "nizamovtimur/rubert-tiny-reports-roads-classification",
    "nizamovtimur/rubert-tiny-reports-another-classification",
]

for model in MODELS:
    pipeline(model=model).save_pretrained(MODELS_PATH+model)
