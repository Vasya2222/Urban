def single_root_words(root_word: str, *other: tuple) -> list[str]:
    other_words = list()
    for item in other:
        if root_word.lower() in item.lower() or item.lower() in root_word.lower():
            other_words.append(item)

    return other_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)