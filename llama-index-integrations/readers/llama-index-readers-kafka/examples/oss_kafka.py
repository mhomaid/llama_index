from llama_index.readers.kafka import KafkaReader

# Configure the KafkaReader
bootstrap_servers = ["localhost:9092"]
topic = "llama_index_test_topic"
group_id = "llama_index_test_group"

# Create an instance of KafkaReader
reader = KafkaReader(
   bootstrap_servers=bootstrap_servers,
   topic=topic,
   group_id=group_id,
)

# Load data from Kafka
documents = reader.load_data()
print(documents)