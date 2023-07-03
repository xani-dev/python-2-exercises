class WordCounter:

    def __init__(self, sentence):
        self.sentence = sentence

    # Returns the number of all the words.
    def count_words(self):
        return (len(self.sentence.split()))

    # Returns the length of the shortest word.
    def get_shortest_word(self):
        shortest = min(self.sentence.split(), key=len)
        return (len(shortest))

    # Returns the length of the longest word.
    def get_longest_word(self):
        shortest = max(self.sentence.split(), key=len)
        return (len(shortest))


sentence = "This is a test of the emergency broadcast system"
word_counter = WordCounter(sentence)
print('Number of words: ', word_counter.count_words())
print('Length of shortest word: ', word_counter.get_shortest_word())
print('Length of longest word: ', word_counter.get_longest_word())
