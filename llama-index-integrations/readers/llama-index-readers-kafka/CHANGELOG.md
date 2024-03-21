# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2024-03-21

### Added
- Kafka reader integration:
  - Updated the notebook to integrate the Kafka reader.
  - Added instructions for installing the required libraries using `requirements.txt`.
  - Updated the code to import the `KafkaReader` class from `llama_index.readers.kafka`.
  - Provided a complete example of using the `KafkaReader` to load data from Kafka, create an index, and perform queries.

### Changed
- Updated the `requirements.txt` file:
  - Added `llama-index`, `llama-index-readers-kafka`, and `confluent-kafka` as dependencies.
- Updated the `__init__.py` file in the `llama_index.readers.kafka` package:
  - Imported the `KafkaReader` class from `llama_index.readers.kafka.base`.
  - Added `KafkaReader` to the `__all__` list to make it available when importing from the package.
- Updated the `mappings.json` file:
  - Added an entry for the `KafkaReader` under the `"readers"` section.
  - Mapped the `"KafkaReader"` key to the `"llama_index.readers.kafka"` import path.

## [0.1.0] - 2024-03-20

### Added
- Created the initial LlamaIndex-readers-kafka integration package structure.
- Implemented the `KafkaReader` class in `base.py` for loading data from Kafka topics into LlamaIndex.
- Added unit tests for the `KafkaReader` class in `tests/test_readers_kafka.py`.
- Included necessary configuration files and documentation:
  - `.gitignore`: Specifies files and directories to be ignored by Git.
  - `BUILD`: Build configuration file for the package.
  - `Makefile`: Makefile for common development tasks.
  - `README.md`: Readme file providing an overview and usage instructions for the package.
  - `pyproject.toml`: Configuration file for the Python project.

### Changed
- Updated the `load_data` method in the `KafkaReader` class to return a list of `Document` objects.
- Modified the unit tests to align with the updated `load_data` method and imports.

### Maintainers
- Mohamed Homaid (mhomaid@gmail.com, mohamed@dataconverse.ai)