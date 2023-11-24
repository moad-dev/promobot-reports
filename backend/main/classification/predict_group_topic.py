from transformers import pipeline


class PredictGroupTopic:
    def __init__(self):
        self.model_group = pipeline("text-classification", "ai_models/nizamovtimur/rubert-base-cased-reports-group-topic-classification", max_length=512)
        self.model_landscaping = pipeline("text-classification", "ai_models/nizamovtimur/rubert-tiny-reports-landscaping-classification")
        self.model_transport = pipeline("text-classification", "ai_models/nizamovtimur/rubert-tiny-reports-transport-classification")
        self.model_garbage = pipeline("text-classification", "ai_models/nizamovtimur/rubert-tiny-reports-garbage-classification")
        self.model_zhkh = pipeline("text-classification", "ai_models/nizamovtimur/rubert-tiny-reports-zhkh-classification")
        self.model_covid = pipeline("text-classification", "ai_models/nizamovtimur/rubert-tiny-reports-covid-classification")
        self.model_social = pipeline("text-classification", "ai_models/nizamovtimur/rubert-tiny-reports-social-service-classification")
        self.model_health = pipeline("text-classification", "ai_models/nizamovtimur/rubert-tiny-reports-health-classification")
        self.model_education = pipeline("text-classification", "ai_models/nizamovtimur/rubert-tiny-reports-education-classification")
        self.model_roads = pipeline("text-classification", "ai_models/nizamovtimur/rubert-tiny-reports-roads-classification")
        self.model_another = pipeline("text-classification", "ai_models/nizamovtimur/rubert-tiny-reports-another-classification")
        self.models = {'Благоустройство': self.model_landscaping,
                  'Общественный транспорт': self.model_transport,
                  'Мусор/Свалки/ТКО': self.model_garbage,
                  'ЖКХ': self.model_zhkh,
                  'Коронавирус': self.model_covid,
                  'Социальное обслуживание и защита': self.model_social,
                  'Здравоохранение/Медицина': self.model_health,
                  'Образование': self.model_education,
                  'Дороги': self.model_roads}

    def predict(self, input) -> tuple[str, str]:
        group = self.model_group(input, truncation=True)[0]
        group_label = group['label']
        if group_label not in self.models.keys():
            return group_label, self.model_another(input, truncation=True)[0]['label']
        return group_label, self.models[group_label](input, truncation=True)[0]['label']
