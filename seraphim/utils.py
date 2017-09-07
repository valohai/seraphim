def emchunken(input, length):
    chunk = []
    for x in input:
        chunk.append(x)
        if len(chunk) == length:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def get_text(soup, selector):
    for tag in soup.select(selector):
        return (tag.text or '').replace('·', ' ').strip()
    return None
