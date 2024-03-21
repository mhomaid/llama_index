# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

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