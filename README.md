# Python Store Project

This is a toy project to showcase unit testing. 

## Setup

1. Make sure you have Python 3.7+ installed. You can download the latest version from [the official website](https://www.python.org/downloads/).

2. Clone the repository or download and extract the project files to a directory on your local machine.

3. (Optional) Create a virtual environment for the project to keep the dependencies isolated:

    ```
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:

        ```
        venv\Scripts\activate
        ```

    - For macOS/Linux:

        ```
        source venv/bin/activate
        ```

5. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

## Running Unit Tests

To run the unit tests, you can use the following command from the project's root directory (`python-store-project`):

```
python -m unittest discover -s tests -p "test_*.py"
```

Alternatively, you can use `pytest` with the following command:

```
pytest tests/
```

### Running Individual Tests

To run an individual test with pytest, use the following command:

```
pytest tests/test_module.py::TestClass::test_method
```

Replace `test_module.py`, `TestClass`, and `test_method` with the appropriate test module, test class, and test method names, respectively.

### Additional pytest Commands

You can also use additional commands with pytest, such as coverage reporting, test parallelization, and various reporting options.

#### Coverage Reporting

To generate a coverage report, use the following command:

```
pytest --cov=store tests/ --cov-report=term-missing
```

To generate an HTML coverage report, use the following command:

```
pytest --cov=store --cov-report=html --cov-report=term-missing
```

#### Test Parallelization

To run tests in parallel, use the following command:

```
pytest -n NUM_WORKERS tests/
```

Replace `NUM_WORKERS` with the number of parallel workers you want to use.

#### Reporting Options

To show a summary of test results, use the following command:

```
pytest -ra tests/
```

To display the slowest test durations, use the following command:

```
pytest --durations=N tests/
```

Replace `N` with the number of slowest test durations you want to display.
