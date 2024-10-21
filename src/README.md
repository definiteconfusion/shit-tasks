# Shit Tasks

This project provides utility classes for handling YAML files, text files, and Base64 encoding/decoding.

## Classes

### Yaml
Handles loading and dumping data to and from a YAML file.

- `__init__(path: str="./config.yaml")`: Initializes the Yaml class with the specified file path.
- `load()`: Loads and returns the data from the YAML file.
- `dump(data: dict)`: Writes the given data to the YAML file.

### Files
Handles reading from and writing to a text file.

- `__init__(path: str="./hello_world.txt")`: Initializes the Files class with the specified file path.
- `read()`: Reads and returns the content of the text file.
- `write(data: str)`: Writes the given string data to the text file.

### Base64
Handles encoding and decoding of Base64 strings.

- `__init__(data: str)`: Initializes the Base64 class with the given string data.
- `encode()`: Encodes the string data to Base64.
- `decode()`: Decodes the Base64 string data back to its original form.