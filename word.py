import re

class Word:

    def __init__(self, word):
        self.passed = word
        loweralpha = "".join([l.lower() for l in word if l.isalpha()])
        self.word = loweralpha
        self.inventory = sorted(list(set(loweralpha)))
        self.lcount = dict([(l,loweralpha.count(l)) for l in loweralpha])

    def __str__(self):
        return f"original word: {self.passed}\nword: {self.word}\nhas letters: {self.inventory}\n"

    # counts how many times each of self's unique letters occurs in word 
    # if the input word contains letters that are not in the inventory, return False
    # else return a list of numbers that represent the occurrences of self's letters in word, in the order of inventory
    def count(self, word):
        count = [0 for l in self.inventory]
        not_in_inventory = []
        for l in word:
            contains_letter = False
            for i in range(len(self.inventory)):
                if l == self.inventory[i]:
                    count[i]+=1
                    contains_letter = True
                    break
            if not contains_letter:
                not_in_inventory.append(l)
        return (count, not_in_inventory)

    def difference(self, word):
        (i_count, i_spare) = self.count(self.word)
        (w_count, w_spare) = self.count(word.word)
        return [i_count[i]-w_count[i] for i in range(len(i_count))]



