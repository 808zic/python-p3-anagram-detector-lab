# your code goes here!
class Anagram:
    def __init__(self, character):
        self.character = character
    
    def match(self, character):
        sorted_character = sorted(self.character)
        return [w for w in character if sorted(w) == sorted_character]
