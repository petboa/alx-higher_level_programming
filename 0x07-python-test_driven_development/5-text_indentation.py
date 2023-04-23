#!/usr/bin/python3
""" This function prints a text with new lines after each . ? and : """


def print_text_with_newlines(text):
    """
    Prints the given text with new lines added after each period, question mark,
    and colon character.

    Args:
        text (str): The text to print.

    Returns:
        None
    """
    last_char = " "
    formatted_text = ""
    
    if text == "":
        print(formatted_text, end='')
        
    if not isinstance(text, str):
        raise TypeError("text must be a string")
        
    for char in text:
        if char == last_char and char == ' ':
            last_char = char
            continue
        if (last_char == '.' or last_char == '?' or last_char == ':') and char == ' ':
            last_char = char
            continue
        if char == '.' or char == '?' or char == ':':
            formatted_text += char + "\n" + "\n"
            last_char = char
        else:
            formatted_text += char
            last_char = char

    print(formatted_text.rstrip(' '), end="")
