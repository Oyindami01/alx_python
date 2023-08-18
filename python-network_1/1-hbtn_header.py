#!/usr/bin/python3

"""
Module to fetch and display the value of the X-Request-Id variable in the response header of a given URL
"""

import requests
import sys

def main():
    """
    Fethches a URL and displays the value of the X-Request-Id
    variable in the response header.
    Usage:
        python script.py <URL>
    Args:
    None(Uses sys.argv to retrieve the URL from the command-line argument)
    Returns:
        None
    """
    
    if len(sys.argv) !=2:
        print("Usage: python script.py <URL>")
        return

    #retrieve the URL from the command-line argument
    url = sys.argv[-1]
    #try:
    #send a GET reqquest to the specified URL
    response = requests.get(url)

    #check if response status code is 200
    if response.status_code == 200:
        #retrieve value of X-Request-Id header drom the response
        x_request_id = response.headers.get('X-Request-Id')

        #check if X-request-Id header exists in the response
        if x_request_id:
            print(x_request_id)
            

if __name__ == "__main__":
    main()