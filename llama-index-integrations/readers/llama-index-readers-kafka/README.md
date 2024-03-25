# LlamaIndex Readers Integration: Kafka
The LlamaIndex Kafka Reader is an integration package that allows loading data from Kafka topics into LlamaIndex for indexing and querying.

## Installation

To install the LlamaIndex Kafka Reader, you can use pip:

```shell
pip install llama-index-readers-kafka

[tool.poetry.dependencies]
llama-index-readers-kafka = "^0.3.0"
```
### Then run poetry install to install the package.

## Usage
Here's a basic example of how to use the LlamaIndex Kafka Reader:

```python
from llama_index import VectorStoreIndex
from llama_index_readers_kafka import KafkaReader

# Configure the KafkaReader
bootstrap_servers = ["localhost:9092"]
topics = ["my_topic"]
group_id = "my_group"
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
index = VectorStoreIndex.from_documents(documents)

# Query the index
query_engine = index.as_query_engine()
response = query_engine.query("What is the main topic of the documents?")

print(response)

# Close the Kafka reader
reader.close()
```

In this example, we configure the KafkaReader with the bootstrap servers, topics, group ID, and security protocol. Then, we create an instance of the KafkaReader and load data from Kafka using the load() method.

The loaded documents are used to create an index using the VectorStoreIndex from LlamaIndex. We can then query the index using a query engine and retrieve relevant information.

Finally, we close the Kafka reader to release any resources.


## Configuration

The KafkaReader supports various configuration options:

- `bootstrap_servers`: A list of Kafka bootstrap servers to connect to.
- `topics`: A list of Kafka topics to subscribe to.
- `group_id`: The consumer group ID.
- `auto_offset_reset`: The auto offset reset strategy. Default is 'latest'.
- `client_id`: The client ID. Default is None.
- `security_protocol`: The security protocol to use. Default is None.
- `sasl_mechanism`: The SASL mechanism to use. Default is None.
- `sasl_username`: The SASL username. Default is None.
- `sasl_password`: The SASL password. Default is None.
- `**kwargs`: Additional keyword arguments to pass to the Kafka consumer.

## Contributing

Contributions to the LlamaIndex Kafka Reader are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

The LlamaIndex Kafka Reader is released under the MIT License.

## Changelog

Please refer to the `CHANGELOG.md` file for a detailed history of changes made to the LlamaIndex Kafka Reader.

## Maintainers

- Mohamed Homaid (mhomaid@gmail.com, mohamed@dataconverse.ai)