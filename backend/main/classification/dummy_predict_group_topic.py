class DummyPredictGroupTopic:
    def predict(self, _: str) -> tuple[str, str]:
        return 'group', 'topic'
