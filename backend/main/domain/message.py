from main.classification.predict_group_topic import PredictGroupTopic
from main.ner.extract_address import extract_addresses
from main.domain.address import Address
from main.domain.processed_message import ProcessedMessage
from main.settings import settings
import uuid

# poor man dependency injection
if settings.dummy_model:
    from main.classification.dummy_predict_group_topic import DummyPredictGroupTopic
    predict_group_topic = DummyPredictGroupTopic()
    from main.classification.dummy_predict_is_trash import DummyPredictIsTrash
    predict_is_trash = DummyPredictIsTrash()
else:
    from main.classification.predict_group_topic import PredictGroupTopic
    predict_group_topic = PredictGroupTopic()
    from main.classification.predict_is_trash import PredictIsTrash
    predict_is_trash = PredictIsTrash()


class Message:
    def __init__(self, text: str):
        self.text = text

    def process(self) -> ProcessedMessage:
        group, topic = predict_group_topic.predict(self.text)
        is_trash = predict_is_trash.predict(self.text)
        return ProcessedMessage(
            uuid=uuid.uuid4().hex,
            text=self.text,
            group=group,
            topic=topic,
            is_trash=is_trash,
            addresses=[
                Address(
                    region=a.get('region'),
                    area=a.get('area', []),
                    settlement=a.get('settlement', []),
                    street=a.get('street', []),
                    building=a.get('building', [])
                ) 
                for a in extract_addresses(self.text)
            ]
        )
        
