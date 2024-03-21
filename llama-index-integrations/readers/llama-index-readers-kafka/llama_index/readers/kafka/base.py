from typing import List, Optional, TypedDict

from llama_index.core.readers.base import BaseReader
from llama_index.core.schema import Document

from confluent_kafka import Consumer, KafkaError

class KafkaReader(BaseReader):
    """Kafka reader class for LlamaIndex.

    This class provides a way to load data from Kafka topics into LlamaIndex.
    """

    def __init__(
        self,
        bootstrap_servers: List[str],
        topic: str,
        group_id: str,
        auto_offset_reset: str = "earliest",
        enable_auto_commit: bool = True,
        max_poll_interval_ms: int = 300000,
        **kwargs,
    ):
        """Initialize the KafkaReader.

        Args:
            bootstrap_servers (List[str]): List of Kafka bootstrap servers.
            topic (str): Kafka topic to read from.
            group_id (str): Consumer group ID.
            auto_offset_reset (str): Auto offset reset strategy. Default is "earliest".
            enable_auto_commit (bool): Whether to enable auto commit. Default is True.
            max_poll_interval_ms (int): Maximum poll interval in milliseconds. Default is 300000.
            **kwargs: Additional keyword arguments to pass to the Kafka consumer.
        """
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.group_id = group_id
        self.auto_offset_reset = auto_offset_reset
        self.enable_auto_commit = enable_auto_commit
        self.max_poll_interval_ms = max_poll_interval_ms
        self.kwargs = kwargs

    def load_data(self) -> List[Document]:
        """Load data from Kafka.

        This method creates a Kafka consumer, subscribes to the specified topic,
        and consumes messages from the topic. It returns the loaded data as a list of Document objects.

        Returns:
            List[Document]: The loaded data from Kafka as a list of Document objects.
        """
        conf = {
            "bootstrap.servers": ",".join(self.bootstrap_servers),
            "group.id": self.group_id,
            "auto.offset.reset": self.auto_offset_reset,
            "enable.auto.commit": self.enable_auto_commit,
            "max.poll.interval.ms": self.max_poll_interval_ms,
        }
        conf.update(self.kwargs)

        consumer = Consumer(conf)
        consumer.subscribe([self.topic])

        loaded_data = []

        try:
            while True:
                msg = consumer.poll(1.0)

                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        raise Exception(msg.error())

                content = msg.value().decode("utf-8")
                document = Document(content)
                loaded_data.append(document)
        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()

        return loaded_data