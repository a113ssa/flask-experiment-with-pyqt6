import re


def remove_markdown(string: str, tag: str = '') -> str:
    """Remove markdown from string."""
    result = re.sub(r'[*_`~]', '', string)
    if tag != '':
        return re.sub(tag, '', result)
    return re.sub(r'[*_`~]', '', string)
