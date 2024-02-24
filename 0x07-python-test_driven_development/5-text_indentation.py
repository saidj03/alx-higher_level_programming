#!/usr/bin/python3

"""prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints a text with specific indentation

    Args:
        text (str): text to indent

    Raises:
        TypeError exception with the message text must be a string

    Returns:
        Nothing
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i], end="")
        else:
            print()
            print()
