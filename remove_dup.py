text = 'The quik quik brown fox jumps over the over lazy dog'


def remove_duplicates(text):
    text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    lst = text.split()
    counter = {}
    i = []
    for word in lst:
        word_counter = counter.get(word)
        if word_counter is None:
            counter[word] = 1
        else:
            counter[word] = word_counter + 1
    for key in counter:
        if counter[key] == 1:
            i.append(key)

    result = ' '.join(i)
    return result


print(remove_duplicates(text))

assert remove_duplicates('The quick brown fox jumps over the lazy dog') == 'The quick brown fox jumps over the lazy dog'
assert remove_duplicates('The quick brown fox. The fox jumps over the lazy dog!') == 'quick brown jumps over the lazy dog'
assert remove_duplicates('The quick brown fox. The fox jumps over the lazy lazy brown dog!') == 'quick jumps over the dog'