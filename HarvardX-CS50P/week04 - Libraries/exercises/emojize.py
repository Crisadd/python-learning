"""Emojize
Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, for instance, :thumbs_up:, which will be automatically converted to 👍. Some programs additionally support aliases, whereby you can more succinctly type, for instance, :thumbsup:, which will also be automatically converted to 👍.

See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.

In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

HINTS:
    - Note that the emoji module comes with two functions, per pypi.org/project/emoji, one of which is emojize, which takes an optional, named parameter called language. You can install it with:
        pip install emoji
"""

# c:\Users\crist\OneDrive\Escritorio\python-learning\.venv\Scripts\python.exe -m pip install emoji
import emoji

user = input("Emoji: ")

print(emoji.emojize(user, language="alias"))

print(f'{emoji.emojize(user, language="alias")}')
