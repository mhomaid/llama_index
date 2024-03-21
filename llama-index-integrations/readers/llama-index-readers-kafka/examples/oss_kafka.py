from llama_index.readers.kafka import KafkaReader

# Configure the KafkaReader
bootstrap_servers = ["localhost:9092"]
topics = ["llama_index_test_topic"]
group_id = "llama_index_test_group"
security_protocol = "PLAINTEXT"

# Create an instance of KafkaReader
reader = KafkaReader(
    bootstrap_servers=bootstrap_servers,
    topics=topics,
    group_id=group_id,
    security_protocol=security_protocol,
)

# Load data from Kafka
documents = reader.load()

# Create an index using the loaded documents
# index = VectorStoreIndex.from_documents(documents)

# Query the index
# query_engine = index.as_query_engine()
# response = query_engine.query("What is the main topic of the documents?")

# print(response)

# Close the Kafka reader
reader.close()