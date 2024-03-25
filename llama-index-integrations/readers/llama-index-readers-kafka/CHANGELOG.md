# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0] - 2024-03-21

### Added
- Support for multiple bootstrap servers
  - The `bootstrap_servers` parameter now accepts a list of strings
  - Bootstrap servers are joined with commas in the consumer configuration

### Changed
- Fixed the `subscribe` method call in the `_create_consumer` method
  - Pass `self.topics` directly to `subscribe` since it's already a list
  - Ensure proper subscription to multiple Kafka topics
- Updated the `_handle_record` method to use the correct `Document` constructor
  - Use the `text` keyword argument instead of `page_content`
  - Match the `Document` class definition from the `llama_index` library
- Improved print statements in the `lazy_load` method
  - Print the loaded document instead of the count
  - Provide more informative output during document loading
- Enhanced code readability
  - Moved the backslash in the `if` condition to the next line
  - Improved overall code formatting and alignment

## [0.2.0] - 2024-03-21

### Added
- Kafka reader integration:
  - Updated the notebook to integrate the Kafka reader
  - Added instructions for installing the required libraries using `requirements.txt`
  - Updated the code to import the `KafkaReader` class from `llama_index.readers.kafka`
  - Provided a complete example of using the `KafkaReader` to load data from Kafka, create an index, and perform queries

### Changed
- Updated the `requirements.txt` file:
  - Added `llama-index`, `llama-index-readers-kafka`, and `confluent-kafka` as dependencies
- Updated the `__init__.py` file in the `llama_index.readers.kafka` package:
  - Imported the `KafkaReader` class from `llama_index.readers.kafka.base`
  - Added `KafkaReader` to the `__all__` list to make it available when importing from the package
- Updated the `mappings.json` file:
  - Added an entry for the `KafkaReader` under the `"readers"` section
  - Mapped the `"KafkaReader"` key to the `"llama_index.readers.kafka"` import path

## [0.1.0] - 2024-03-20

### Added
- Created the initial LlamaIndex-readers-kafka integration package structure
- Implemented the `KafkaReader` class in `base.py` for loading data from Kafka topics into LlamaIndex
- Added unit tests for the `KafkaReader` class in `tests/test_readers_kafka.py`
- Included necessary configuration files and documentation:
  - `.gitignore`: Specifies files and directories to be ignored by Git
  - `BUILD`: Build configuration file for the package
  - `Makefile`: Makefile for common development tasks
  - `README.md`: Readme file providing an overview and usage instructions for the package
  - `pyproject.toml`: Configuration file for the Python project

### Changed
- Updated the `load_data` method in the `KafkaReader` class to return a list of `Document` objects
- Modified the unit tests to align with the updated `load_data` method and imports

### Maintainers
- Mohamed Homaid (mhomaid@gmail.com, mohamed@dataconverse.ai)