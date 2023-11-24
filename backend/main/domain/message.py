from main.classification.predict_group_topic import PredictGroupTopic
from main.ner.extract_address import extract_addresses
from main.domain.address import Address
from main.domain.processed_message import ProcessedMessage
from main.settings import settings
import uuid

if settings.dummy_model:
    from main.classification.dummy_predict_group_topic import DummyPredictGroupTopic
    predict_group_topic = DummyPredictGroupTopic()
else:
    from main.classification.predict_group_topic import PredictGroupTopic
    predict_group_topic = PredictGroupTopic()


class Message:
    def __init__(self, text: str):
        self.text = text

    def process(self) -> ProcessedMessage:
        group, topic = predict_group_topic.predict(self.text)
        return ProcessedMessage(
            uuid=uuid.uuid4().hex,
            text=self.text,
            group=group,
            topic=topic,
            addresses=[
                Address(
                    region=a['region'],
                    area=a['area'],
                    settlement=a['settlement'],
                    street=a['street'],
                    building=a['building']
                ) 
                for a in extract_addresses(self.text)
            ]
        )
        