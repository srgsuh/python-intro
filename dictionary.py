from sortedcontainers import SortedKeyList

class Dictionary:
    def __init__(self):
        self.__set: set[str] = set()
        self.__sorted_key_list: SortedKeyList = SortedKeyList(
            key=str.casefold
        )

    def add_word(self, word: str) -> None:
        word_low: str = word.casefold()
        if word_low in self.__set:
            raise ValueError(f"Word with the case fold value '{word_low}' already exists")
        self.__set.add(word_low)
        self.__sorted_key_list.add(word)

    def get_all_words(self) -> list[str]:
        return list(self.__sorted_key_list)

    def get_words_by_prefix(self, prefix: str) -> list[str]:
        prefix_right: str = prefix + chr(0xFFFF)
        left: int = self.__sorted_key_list.bisect_left(prefix)
        right: int = self.__sorted_key_list.bisect_right(prefix_right)
        return list(self.__sorted_key_list[left:right])

if __name__ == '__main__':
    d: Dictionary = Dictionary()
    d.add_word("Absolute")
    d.add_word("ABracadabra")
    d.add_word("aBSURD")
    d.add_word("aBSzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    d.add_word("ABT")

    print(f"All words: {d.get_all_words()}")
    print(f"All words with the prefix 'abs': {d.get_words_by_prefix("abs")}")
    print(f"All words with the prefix 'ABS': {d.get_words_by_prefix("ABS")}")
    print(f"All words with the prefix '': {d.get_words_by_prefix("")}")