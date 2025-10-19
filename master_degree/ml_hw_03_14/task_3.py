dict = {}
filename = input()

with open(filename, encoding="utf-8") as f:
    for line in f:
        for word in line.rstrip('\n').split(" "):
            if word != "":
                dict[word] = dict.get(word, 0) + 1

sorted_dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_dict:
    print(f"{count} {word}")
