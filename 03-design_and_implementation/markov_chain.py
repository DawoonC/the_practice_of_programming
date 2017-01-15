from collections import defaultdict
import random


def markov_chain(input_text):
    MAXGEN = 10000
    NONWORD = '\n'
    pref1 = pref2 = NONWORD
    words = input_text.split()
    statetab = defaultdict(list)
    result = []
    # build {prefix: [suffix,...]} dictionary
    for word in words:
        statetab[' '.join((pref1, pref2))].append(word)
        pref1, pref2 = pref2, word
    statetab[' '.join((pref1, pref2))].append(NONWORD)
    # generate random text from the dictionary
    pref1 = pref2 = NONWORD
    for _ in range(MAXGEN):
        suf_list = statetab[' '.join((pref1, pref2))]
        if len(suf_list) > 0:
            suf = random.choice(suf_list)
            if suf == NONWORD:
                break
            result.append(suf)
            pref1, pref2 = pref2, suf
    print ' '.join(result)


text = '''Show your flowcharts and conceal your tables and I will be mystified. Show your tables and your flowcharts will be obvious. (end)'''

# test
markov_chain(text)
