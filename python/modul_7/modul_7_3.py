class WordsFinder():
    file_names = []

    def __init__(self, *args):
        for item in args:
            self.file_names.append(item)

    def get_all_words(self) -> dict[str: list[str]]:
        all_words: dict[str: list[str]] = dict()
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()
            all_words[file] = self.delete_punctuation(text).lower().split()
        return all_words

    def find(self, word: str):
        result = dict()

        for file, item in self.get_all_words().items():
            result[file] = item.index(word.lower()) if word.lower() in item else None

        return result

    def count(self, word):
        result = dict()

        for file, item in self.get_all_words().items():
            result[file] = self.count_words(item, word)

        return result

    def count_words(self, items, word):
        return items.count(word.lower()) if word.lower() in items else None

    def delete_punctuation(self, text: str):
        list_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        new_text = text
        for punctuation in list_punctuation:
            new_text = new_text.replace(punctuation, '' if punctuation != ' - ' else ' ')

        return new_text

finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
