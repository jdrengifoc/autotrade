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

2. Open the `.env` file and replace `your_api_key_here` with your actual `polygon.io` API key:
    ```
    POLYGON_API_KEY=your_api_key_here
    ```

3. The project will automatically load the API key from the `.env` file when you run it.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Disclaimer

This project is for educational purposes only. Trading in the stock market involves risk, and you should not trade with money you cannot afford to lose.

## Contact

For any questions or suggestions, please open an issue or contact me at jdrengifoc@eafit.edu.co.