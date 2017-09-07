def emchunken(input, length):
    chunk = []
    for x in input:
        chunk.append(x)
        if len(chunk) == length:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def get_text(soup, selector, attr=None):
    for tag in soup.select(selector):
        text = (tag[attr] if attr else (tag.text or ''))
        return text.replace('·', ' ').strip()
    return None
