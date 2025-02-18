r"\bun\w*an\b"
import re  # We need the regular expressions module


def find_un_an_pattern(text):
    """
    This function finds occurrences of words that:
    - Start with 'un'
    - Have any number of letters in between
    - End with 'an'

    :param text: The input text to search in
    :return: The number of matches found
    """
    pattern = r"\bun\w*an\b"  # Defining the search pattern
    matches = re.findall(pattern, text)  # Finding all matches
    return len(matches)  # Returning the count of matches



text = "I know an uncertain man who is an unbroken urban musician but not an unitarian." #asked chat for random sentence
print(find_un_an_pattern(text))  # Output: 3 (uncertain, unbroken, urban)
