#!/usr/bin/python3

def multiple_returns(sentance):
    if sentance == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
