# Random Objects Generator and Identifier

This project implements a solution for generating and identifying random objects as specified in the challenge requirements. It consists of three main components:

## Project Structure

```
.
├── random_object_generator.py    # Core class for generating random objects
├── object_type.py                # Enum and utilities for object type identification
├── write_random_objects_to_file.py  # Challenge A: Generates a 10MB file of random objects
├── identify_random_objects_from_file.py  # Challenge B: Identifies objects from the file
├── Dockerfile                    # For containerizing Challenge B
├── docker-compose.yaml           # For running the containerized solution
├── random_objects.txt            # Output file from Challenge A (generated)
└── results.txt                   # Output file from Challenge B/C (generated)
```

## Challenge A: Random Objects Generator

Generates a 10MB file containing four types of random objects separated by commas:
- Alphabetical strings (e.g., "abcXYZ")
- Real numbers (e.g., "123.456")
- Integers (e.g., "42")
- Alphanumerics with random spaces before and after (e.g., "   a1b2c3   ")

### Usage

```bash
python write_random_objects_to_file.py
```

This will generate a file named `random_objects.txt` in the current directory.

## Challenge B: Random Objects Identifier

Reads the file generated in Challenge A and prints each object along with its type to the console. Spaces before and after alphanumeric objects are stripped during processing.

### Usage

```bash
python identify_random_objects_from_file.py
```

## Challenge C: Dockerized Solution

A Docker container that reads the output from Challenge A and executes the program from Challenge B. The output is saved to a file and exposed to the host machine.

### Usage

1. Build and run the Docker container using Docker Compose:

```bash
docker-compose up
```

2. The results will be saved to `results.txt` in the project directory.

## Implementation Details

### Random Object Generator

The `RandomObjectGenerator` class provides methods to generate different types of random objects:
- `alphabetical_object()`: Generates random alphabetical strings
- `real_object()`: Generates random real numbers
- `integer_object()`: Generates random integers
- `alpha_numeric_object()`: Generates random alphanumeric strings with spaces

### Object Type Identification

The `ObjectType` enum provides a way to categorize objects and includes a static method `get_from_object()` that uses regular expressions to determine the type of a given object.

## Requirements

- Python 3.9+
- Docker (for Challenge C)
- Docker Compose (for Challenge C)

## Running the Complete Solution

1. Generate the random objects file:
```bash
python write_random_objects_to_file.py
```

2. Either run the identifier directly:
```bash
python identify_random_objects_from_file.py
```

3. Or use Docker to process the file:
```bash
docker-compose up
```

The results will be available in `results.txt`.