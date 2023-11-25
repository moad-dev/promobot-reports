from transformers import pipeline


class PredictIsTrash:
    def __init__(self):
        self.model_is_trash = pipeline("text-classification", "ai_models/danil7/rubert-tiny-reports-is-trash-classification", max_length=512)

    def predict(self, input) -> str:
        is_trash = self.model_is_trash(input, truncation=True)[0]
        is_trash_label = is_trash['label']
        print(is_trash_label)
        return is_trash_label == 'wrong'
