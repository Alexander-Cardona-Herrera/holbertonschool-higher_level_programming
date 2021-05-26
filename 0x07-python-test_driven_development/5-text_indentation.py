#!/usr/bin/python3
"""
For this function you can't use any type of characters bisides str.

text can be of any longitud.
"""


def text_indentation(text):
    """
    Add to blank lines at the end of . ; ? chars.
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    new_text = "\n".join(i.strip() for i in text.split('\n'))

    print(new_text, end='')
