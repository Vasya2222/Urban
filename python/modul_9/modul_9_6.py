def all_variants(text):
    for size in range(len(text)):
        for l in range(len(text)-size):
            yield text[l:l+size+1]


text = input()

for i in all_variants(text):
    print(i)
