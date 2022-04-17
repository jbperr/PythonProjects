import enchant
import itertools

d = enchant.Dict("en_US")

letlist = [
    input("First letter: "),
    input("Second letter: "),
    input("Third letter: "),
    input("Fourth letter: "),
    input("Fifth letter: "),
    input("Sixth letter: "),
]

curword = "".join(letlist)
wordlist = []

words = list(itertools.permutations(letlist))

for i in range(len(words)):
    words[i] = "".join(words[i])

while len(curword) >= 3:
    for i in range(len(words)):
        if len(words[i]) >= 3:
            words.append(words[i][:-1])
            curword = words[-1]

words = list(set(words))

final_list = []

for i in range(len(words)):
    if d.check(words[i]) == True:
        final_list.append(words[i])

print(sorted([w for w in final_list if len(w) >= 3]))
