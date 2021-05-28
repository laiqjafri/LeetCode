from collections import Counter


def can_be_built(word, letters):
    letters_counter = Counter(letters)
    word_counter = Counter(word)
    for c, count in word_counter.items():
        if count > letters_counter[c]:
            return False
    return True


def longest_possible_word(words, letters):
    possible_words = [word for word in words if can_be_built(word, letters)]
    max_length = max(len(word) for word in possible_words)
    return [word for word in possible_words if len(word) == max_length]

print(longest_possible_word(['to', 'banana', 'hello', 'toes', 'toe', 'dogs', 'whatever', 'godess'], "osetodg"))