def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Initialize variables to keep track of the best key and score
    best_key = None
    best_score = float('-inf')  # Initialize to negative infinity to handle negative scores

    # Iterate through the items in the dictionary
    for key, value in a_dictionary.items():
        # Update the best_key and best_score if a higher score is found
        if value > best_score:
            best_key = key
            best_score = value

    return best_key