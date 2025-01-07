# AutoTrade

AutoTrade is a Python project designed to assist with trading in the NYSE, UK, and DE stock markets. This project leverages the polygon.io API to retrieve market data and explores the potential use of machine learning for trading strategies.

## Features

- Retrieve real-time and historical market data from polygon.io
- Exploring...

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/autotrade.git
    ```

2. Navigate to the project directory:
    ```bash
    cd autotrade
    ```

3. Install Poetry if you haven’t already:
    ```bash
    brew install poetry
    ```

4. Set up the project dependencies using Poetry:
    ```bash
    poetry install
    ```

    This will install any dependencies specified in the `pyproject.toml` file. If no dependencies are listed, you can skip this step for now.

5. Activate the virtual environment:
    ```bash
    poetry shell
    ```

    Now you can run the project within the Poetry-managed virtual environment.


## Setting Up API Keys

This project requires an API key from `polygon.io` to function properly.

1. Copy the example `.env` file:
    ```bash
    cp .env.example .env
    ```

2. Open the `.env` file and replace `your_api_key_here` with your actual `polygon.io` API key and your XTB credentials:
    ```
    POLYGON_API_KEY=your_api_key_here

    ACCOUNTS_XTB=[
    {"name": "JohnDoe", "username": "johndoe_user", "password": "johndoe_password"},
    {"name": "JaneSmith", "username": "janesmith_user", "password": "janesmith_password"}
]
    ```

3. The project will automatically load the API key from the `.env` file when you run it.


## Running AutoTrade

To run the AutoTrade project using Poetry, follow these steps:

1. Ensure you are in the project directory:
    ```bash
    cd autotrade
    ```

2. Run the main script:
    ```bash
    poetry run python -m autotrade
    ```


## Testing

Follow these steps to run the tests for this project:

### 1. Writing Tests
- Test functions should begin with `test_` to be automatically discovered by `pytest`.
- Tests should be placed in the `tests/` directory.

### 2. Running Tests with `pytest`
To run all the tests in the project, use the following command:

```bash
poetry run pytest
```

This command will automatically discover and run all tests located in the `tests/` directory.

### 3. Running Tests with Debugging Output
To see `print()` statements and debug output during test execution, use the `-s` flag to disable pytest's output capturing:

```bash
poetry run pytest -s
```

This will allow you to see any `print()` statements in the terminal.

### 4. Running Tests for Specific Markers
If you have tests marked with specific markers (e.g., `@pytest.mark.env`), you can run only those tests by using the `-m` flag. For example, to run tests marked with `env`:

```bash
poetry run pytest -m env
```

### 5. Running Tests for Specific Test Files
To run a specific test file, you can provide the file path directly:

```bash
poetry run pytest tests/test_env.py  # Run a specific test file
```

To run all tests in the `tests/` directory:

```bash
poetry run pytest tests/  # Run all tests in the tests directory
```


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Disclaimer

This project is for educational purposes only. Trading in the stock market involves risk, and you should not trade with money you cannot afford to lose.

## Contact

For any questions or suggestions, please open an issue or contact me at jdrengifoc@eafit.edu.co.