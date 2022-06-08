from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from event_listeners import (
    FileObserver, LongestRowObserver, LongestWordObserver, WordCountObserver, RowWithLongestWordObserver
)


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: FileObserver) -> None:
        pass

    @abstractmethod
    def detach(self, observer: FileObserver) -> None:
        pass

    @abstractmethod
    def notify(self, row: str) -> None:
        pass


class FileReader(Subject):
    _observers: List[FileObserver] = []

    def attach(self, observer: FileObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: FileObserver) -> None:
        self._observers.remove(observer)

    def notify(self, row: str) -> None:
        for observer in self._observers:
            observer.update(row)

    def process_file(self, filename) -> None:
        try:
            with open(filename, "r") as f:
                print("Started reading file")
                for row in f.readlines():
                    print("  Line:", row.strip())
                    self.notify(row.strip())
                print("Finished reading file")
        except Exception:
            print("Something went wrong. This file doesn't exist.")


if __name__ == "__main__":
    filename = "resource.txt"

    file_reader = FileReader()
    longest_row_observer = LongestRowObserver()
    longest_word_observer = LongestWordObserver()
    row_with_longest_word_observer = RowWithLongestWordObserver()
    word_count_observer = WordCountObserver()

    file_reader.attach(longest_row_observer)
    file_reader.attach(longest_word_observer)
    file_reader.attach(row_with_longest_word_observer)
    file_reader.attach(word_count_observer)

    file_reader.process_file(filename)
    print(
        f"Longest row: {longest_row_observer.get_result()}\n"
        f"Longest word: {longest_word_observer.get_result()}\n"
        f"Row with longest word: {longest_word_observer.get_result()}\n"
        f"# of words in file: {word_count_observer.get_result()}"
    )
