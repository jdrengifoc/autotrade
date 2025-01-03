from autotrade import POLYGON_API_KEY
from autotrade.utils import check_ticker_available
from polygon import RESTClient

def main():
    #tickers = ['NG', 'I:SPX', 'X:EURUSD']
    #client = RESTClient(api_key=POLYGON_API_KEY)
    if check_ticker_available('I:3NGS'):
        print('Ticker exists')
    else:
        print('Ticker does not exist')



if __name__ == "__main__":
    main()