#!/usr/bin/python3
"""
GitHub User ID Script

This script takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user ID.

"""

import sys
import requests

def main():
    """
    Uses Basic Authentication with a personal access token to access the Github API
    and display the Github user ID.

    Usage:
        python github_user_id.py <username> <personal_access_token>
        
    Args:
        <username>: Your Github username.
        <personal_access_token>: Your github personal access token.

    Returns:
        None
    """

    #retrieve github username and personal access token from the command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    #create the basic authentication header using the personal access token
    auth = (username, token)

    try:
        #send a GET request to the Github API to retrieve user information
        response =  requests.post('http://api.github.com/user', auth=auth)

        #Check if the response status code is 200
        if response.status_code == 200:
            user_info = response.json()
            user_id = user_info['id']
            print(user_id)
        else:
            print("None")

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

if __name__ == "__main__":
    main()