from collections import defaultdict
import random


class Prefix(object):
    def __init__(self, n, dummy_str):
        self.pref = []
        for _ in range(n):
            self.pref.append(dummy_str)
    #
    def get_repr(self):
        return ' '.join(self.pref)


class Chain(object):
    def __init__(self):
        self.NPREF = 2
        self.NONWORD = '\n'
        self.statetab = defaultdict(list)
        self.prefix = Prefix(self.NPREF, self.NONWORD)
        self.result = []
    #
    def build(self, input_text):
        words = input_text.split()
        for word in words:
            self.add(word)
        self.add(self.NONWORD)
    #
    def add(self, word):
        suf = self.statetab[self.prefix.get_repr()]
        suf.append(word)
        if len(self.prefix.pref) > 0:
            self.prefix.pref.pop(0)
            self.prefix.pref.append(word)
    #
    def generate(self, nwords):
        prefix = Prefix(self.NPREF, self.NONWORD)
        for _ in range(nwords):
            suf_list = self.statetab[prefix.get_repr()]
            if len(suf_list) > 0:
                suf = random.choice(suf_list)
                if suf == self.NONWORD:
                    break
                self.result.append(suf)
                prefix.pref.pop(0)
                prefix.pref.append(suf)
        print ' '.join(self.result)


class Markov(object):
    def __init__(self):
        self.MAXGEN = 10000
    #
    def main(self, input_text):
        chain = Chain()
        nwords = self.MAXGEN
        chain.build(input_text)
        chain.generate(nwords)


text = '''Show your flowcharts and conceal your tables and I will be mystified. Show your tables and your flowcharts will be obvious. (end)'''

# test
Markov().main(text)
