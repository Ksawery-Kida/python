# szybkie cwiczenie - stringi i listy

def count_vowels(text):
    vowels = "aeiouyAEIOUY"
    return sum(1 for ch in text if ch in vowels)


def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


if __name__ == "__main__":
    sample = "Nauka Pythona idzie do przodu"
    print(count_vowels(sample))
    print(reverse_words(sample))
