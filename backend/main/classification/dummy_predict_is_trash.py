import random

class DummyPredictIsTrash:
    def predict(self, _: str) -> str:
        return random.randrange(0, 2)
