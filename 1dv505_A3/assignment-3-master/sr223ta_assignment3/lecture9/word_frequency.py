


class QuadHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.count = 0

    def hash_function(self, key):
        return hash(key) % self.size



    def insert(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i * i) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = WordFrequency(key)
                self.count += 1
                return
            elif self.table[new_index].word == key:
                self.table[new_index].frequency += 1
                return

    def search(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i * i) % self.size
            if self.table[new_index] is None:
                return None
            elif self.table[new_index].word == key:
                return self.table[new_index]



class WordFrequency:
    def __init__(self, word):
        self.word = word
        self.frequency = 1

    def __str__(self):
        return f'{self.word}: {self.frequency}'

def clean_word(word):
    return ''.join(char.lower() for char in word if char.isalpha())

def read_and_analyse_text(filename):
    word_table = QuadHash(101)
    lovecraft_terms = {'cthulhu', 'necronomicon', 'nyarlathotep', 'yuggoth', 'kadath', 'azathoth'}

    try:
        with open(filename, 'r') as file:
            for line in file:
                for word in line.split():
                    cleaned_word = clean_word(word)
                    if cleaned_word in lovecraft_terms:
                        word_table.insert(cleaned_word)
        return word_table
    except FileNotFoundError:
        print(f'Error: Could not find file {filename}')
        return None

word_table = read_and_analyse_text('lovecraft.txt')
if word_table:
    print('Here are the frequencies of classic Lovecraftian terms')
    print('-' * 54)
    for item in word_table.table:
        if item is not None:
            print(f'{item.word.capitalize()}: {item.frequency} occurrences')

