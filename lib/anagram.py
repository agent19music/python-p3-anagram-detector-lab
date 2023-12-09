#!/usr/bin/env python3
# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word_characters = sorted([letter for letter in word])
    def match(self, word_list):
        match_word_list = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_characters:
                match_word_list.append(word)

        return match_word_list

one_instance = Anagram('listen')
print(one_instance.match(['enlist', 'google', 'inlets', 'banana']))  # Output: ['enlist', 'inlets']

