from abc import abstractmethod, ABC
import re
from typing import List


def line2words(line: str) -> List[str]:
    return re.split(r"[,.?!]? +", line)


class FileObserver(ABC):
    @abstractmethod
    def update(self, row: str) -> None: pass


class LongestRowObserver(FileObserver):
    _row = ""

    def update(self, row: str) -> None:
        if len(self._row) < len(row):
            print("   LongestRowObserver updated")
            self._row = row

    def get_result(self):
        return self._row


class LongestWordObserver(FileObserver):
    _word = ""

    def update(self, row: str) -> None:
        word = max(line2words(row), key=len)
        if len(self._word) < len(word):
            print("   LongestWordObserver updated")
            self._word = word

    def get_result(self):
        return self._word


class WordCountObserver(FileObserver):
    _word_count = 0

    def update(self, row: str) -> None:
        print("   WordCountObserver updated")
        self._word_count += len(line2words(row))

    def get_result(self):
        return self._word_count


class RowWithLongestWordObserver(FileObserver):
    _row = ""
    _word = ""

    def update(self, row: str) -> None:
        word = max(line2words(row), key=len)
        if len(self._word) < len(word):
            self._word = word
            self._row = row
            print("   RowWithLongestWordObserver updated")

    def get_result(self):
        return self._row
