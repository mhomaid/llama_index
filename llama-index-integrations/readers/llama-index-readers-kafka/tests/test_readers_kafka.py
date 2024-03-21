import pytest
import unittest
from unittest.mock import MagicMock, patch

from llama_index.core.readers.base import BaseReader
from llama_index.readers.kafka.base import KafkaReader
from llama_index.core.schema import Document
def test_class():
    names_of_base_classes = [b.__name__ for b in KafkaReader.__mro__]
    assert BaseReader.__name__ in names_of_base_classes

def test_load_data():
    # Mock the behavior of the Kafka consumer
    mock_msg1 = MagicMock()
    mock_msg1.error.return_value = None
    mock_msg1.value.return_value = b"Test message 1"

    mock_msg2 = MagicMock()
    mock_msg2.error.return_value = None
    mock_msg2.value.return_value = b"Test message 2"

    with patch("llama_index.readers.kafka.base.Consumer") as mock_consumer:
        mock_consumer.return_value.poll.side_effect = [mock_msg1, mock_msg2, None]

        # Create an instance of KafkaReader
        reader = KafkaReader(
            bootstrap_servers=["localhost:9092"],
            topic="test_topic",
            group_id="test_group",
        )

        # Call the load_data method
        loaded_data = reader.load_data()

        # Assert the expected behavior
        assert len(loaded_data) == 2
        assert isinstance(loaded_data[0], Document)
        assert loaded_data[0].text == "Test message 1"
        assert isinstance(loaded_data[1], Document)
        assert loaded_data[1].text == "Test message 2"

        mock_consumer.return_value.subscribe.assert_called_once_with(["test_topic"])
        mock_consumer.return_value.close.assert_called_once()

def test_load_data_error():
    with patch("llama_index.readers.kafka.base.Consumer") as mock_consumer:
        # Mock the behavior of the Kafka consumer to raise an error
        mock_msg = MagicMock()
        mock_msg.error.return_value = MagicMock(code=MagicMock(return_value=999))

        mock_consumer.return_value.poll.return_value = mock_msg

        # Create an instance of KafkaReader
        reader = KafkaReader(
            bootstrap_servers=["localhost:9092"],
            topic="test_topic",
            group_id="test_group",
        )

        # Call the load_data method and assert that it raises an exception
        with pytest.raises(Exception):
            reader.load_data()

        mock_consumer.return_value.close.assert_called_once()