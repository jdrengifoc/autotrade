from autotrade import POLYGON_API_KEY, get_xtb_credentials
#import json
import os

def main():
    credentials = get_xtb_credentials("juan")
    print(credentials['email'])

if __name__ == "__main__":
    main()