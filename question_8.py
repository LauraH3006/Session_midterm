def is_valid_url(url):
    """
    Checks if a given string is a valid URL.
    A valid URL starts with 'http://' or 'https://' and contains at least one '.'

    :param url: string to check
    :return: True if valid, False otherwise
    """
    if (url.startswith("http://") or url.startswith("https://")) and ("." in url):
        return True
    else:
        return False


# lets test if it actually works
print(is_valid_url("http://example.com"))  # True
print(is_valid_url("https://google.com"))  # True
print(is_valid_url("ftp://example.com"))  # False (wrong as it uses ftp://)
print(is_valid_url("example.com"))  # False (missing http)
print(is_valid_url("http://example"))  # False (no dot)
