def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (0, None)  # Return a tuple with length 0 and first character as None

    # If the sentence is not empty, return the tuple with length and first character
    return (len(sentence), sentence[0])