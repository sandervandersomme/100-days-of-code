



def is_palindrome(text):
    return text == ''.join(list(reversed(text)))


def is_symmmetrical(text):
    return text[:-(-len(text)//2)] == text[len(text)//2:]


def reverse_sentence(text):
    return ' '.join(reversed(text.split(' ')))


def remove_ith_char(text, i):
    return text[:i] + text[i+1:]


def contains_string(text, substring):
    return substring in text


def frequency_of_words(text):
    vocab = text.split()
    return {word : vocab.count(word) for word in vocab}


def snake_to_pascal(text):
    return text.replace("_", " ").title().replace(" ", "")

if __name__ == '__main__':
    print(is_palindrome("reinier"))
    print(is_symmmetrical("yoyo"))
    print(reverse_sentence("This is a test"))
    print(remove_ith_char("This is a test", 6))
    print(contains_string("This is a test", "is a"))
    print(frequency_of_words("This is not a test A meteorite is going to hit the earth This is a final warning."))
    print(snake_to_pascal("geeks_for_geeks"))
