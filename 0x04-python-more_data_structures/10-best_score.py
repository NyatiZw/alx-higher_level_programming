#!/usr/bin/python3

# Function that returns a key with biggest integer value
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
