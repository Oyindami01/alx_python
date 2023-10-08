import sys
import os

def user_info(user_id):
    try:
        # Check if the CSV file exists
        filename = str(user_id) + ".csv"
        if os.path.isfile(filename):
            # Read the CSV file and perform the necessary operations
            with open(filename, 'r') as f:
                # Your code to process the CSV file goes here
                pass
        else:
            print(f"CSV file for user ID {user_id} not found.")
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main_1.py <user_id>")
    else:
        user_id = int(sys.argv[1])
        user_info(user_id)
