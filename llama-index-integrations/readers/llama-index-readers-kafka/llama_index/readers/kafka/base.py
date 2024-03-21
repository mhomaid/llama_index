from typing import Any, Iterator, List, Optional
from llama_index.core.readers.base import BaseReader
from llama_index.core.schema import Document
from confluent_kafka import Consumer, KafkaError, KafkaException

def error_cb(err):
    print("Client error: {}".format(err))
    if err.code() == KafkaError._ALL_BROKERS_DOWN or err.code() == KafkaError._AUTHENTICATION:
        raise KafkaException(err)

class KafkaReader(BaseReader):
    def __init__(
        self,
        bootstrap_servers: List[str],
        topics: List[str],
        group_id: str,
        auto_offset_reset: str = 'latest',
        client_id: Optional[str] = None,
        security_protocol: Optional[str] = None,
        sasl_mechanism: Optional[str] = None,
        sasl_username: Optional[str] = None,
        sasl_password: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        if not bootstrap_servers:
            raise ValueError("bootstrap_servers cannot be empty")
        self.bootstrap_servers = bootstrap_servers
        self.topics = topics
        self.group_id = group_id
        self.auto_offset_reset = auto_offset_reset
        self.client_id = client_id
        self.security_protocol = security_protocol
        self.sasl_mechanism = sasl_mechanism
        self.sasl_username = sasl_username
        self.sasl_password = sasl_password
        self.consumer_config = {
            'bootstrap.servers': ','.join(self.bootstrap_servers),
            'group.id': self.group_id,
            'client.id': self.client_id,
            'auto.offset.reset': self.auto_offset_reset,
            'error_cb': error_cb,
            **kwargs,
        }
        if self.security_protocol:
            self.consumer_config['security.protocol'] = self.security_protocol
        if self.sasl_mechanism:
            self.consumer_config['sasl.mechanism'] = self.sasl_mechanism
            self.consumer_config['sasl.username'] = self.sasl_username
            self.consumer_config['sasl.password'] = self.sasl_password
        self.consumer = None

    def _create_consumer(self):
        self.consumer = Consumer(self.consumer_config)
        self.consumer.subscribe(self.topics)

    def _handle_record(self, record: Any, id: Optional[str]) -> Document:
        return Document(text=record.value().decode('utf-8'))

    def lazy_load(self) -> Iterator[Document]:
        if not self.consumer:
            self._create_consumer()
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                break
            if msg.error():
                if msg.error().code() == KafkaError._ALL_BROKERS_DOWN or \
                        msg.error().code() == KafkaError._AUTHENTICATION:
                    raise KafkaException(msg.error())
                else:
                    print(f"Consumer error: {msg.error()}")
                continue
            document = self._handle_record(msg, str(msg.offset()))
            yield document

    def load(self) -> List[Document]:
        documents = list(self.lazy_load())
        return documents

    def close(self):
        if self.consumer:
            self.consumer.close()