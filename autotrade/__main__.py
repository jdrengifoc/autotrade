from autotrade import POLYGON_API_KEY, get_xtb_credentials
from autotrade.xAPIConnector import APIClient, loginCommand
import pandas as pd
import pytz
from datetime import datetime

def main():
    # Login.
    credentials = get_xtb_credentials("mami")
    client = APIClient()
    login_response = client.execute(loginCommand(credentials['email'], credentials['password']))
    
    if not login_response['status']:
        print("Error: ", login_response['errorCode'])
    else:
        print("Login successful")
        stream_session_id = login_response['streamSessionId']

    # Chart range request
    start_time = datetime(2025, 1, 7, 0).timestamp() * 1000
    end_time = datetime(2025, 1, 7, 4, 23).timestamp() * 1000
    chart_range_request = {
        "command": "getChartRangeRequest",
        "arguments": {
            "info": {
                "symbol": "NATGAS",
                "start": start_time,
                "end": end_time,
                "period": 1
            }
        }
    }
    chart_range_response = client.execute(chart_range_request)

    if not chart_range_response['status']:
        print("Error: ", chart_range_response['errorCode'])

    candle_data = chart_range_response['returnData']['rateInfos']
    df = pd.DataFrame(candle_data)
    # Time where? Time is number of milliseconds from 01.01.1970, 00:00 GMT (same as UTC).
    # - ctmString is one hour ahead of ctm.
    # The open price is wrong? The real price  is the open price divided by 1000

    # Define the timezone for Colombia
    colombia_tz = pytz.timezone('America/Bogota')

    # Convert 'ctm' (milliseconds since epoch) to datetime
    df['datetime'] = pd.to_datetime(df['ctm'], unit='ms')

    # Convert to Colombia's time zone
    df['colombia_time'] = df['datetime'].dt.tz_localize('UTC').dt.tz_convert(colombia_tz)

    print(df.tail())

if __name__ == "__main__":
    main()