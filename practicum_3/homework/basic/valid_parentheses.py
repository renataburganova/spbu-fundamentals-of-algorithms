from typing import Any

import yaml
import numpy as np
from numpy.typing import NDArray

from src.common import ProblemCase


class Stack:
    """LIFO queue"""

    def __init__(self, max_n: int, dtype: Any) -> None:
        self._array: NDArray = np.zeros((max_n,), dtype=dtype)  # internal array
        self._top_i: int = -1  # index of the most recently inserted element

    def empty(self) -> bool:
        return self._top_i == -1

    def push(self, x: Any) -> None:
        """Complexity: O(1)"""
        self._top_i += 1
        self._array[self._top_i] = x

    def pop(self) -> Any:
        """Complexity: O(1)"""
        if self.empty():
            raise StackUnderflowException("Stack is empty")
        else:
            top_elem = self._array[self._top_i]
            self._top_i -= 1
            return top_elem



class StackUnderflowException(BaseException):
    pass


class StackOverflowException(BaseException):
    pass


def get_starting_symbol(sym: str) -> str:
    if sym == ")":
        return "("
    elif sym == "]":
        return "["
    elif sym == "}":
        return "{"
    else:
        raise ValueError(f'Unknown parenthesis: "{sym}"')


def are_parentheses_valid(s: str) -> bool:
    stack = Stack(len(s), str)
    for sym in s:
        if sym in "([{":
            stack.push(sym)
        elif sym in ")]}":
            if stack.empty():
                return False
            else:
                if stack.pop() != get_starting_symbol(sym):
                    return False
    return stack.empty()


if __name__ == "__main__":
    # Let's solve Valid Parentheses problem from leetcode.com:
    # https://leetcode.com/problems/valid-parentheses/
    cases = []
    with open("C:/IT/algorithms/spbu-fundamentals-of-algorithms/practicum_3/homework/basic/valid_parentheses_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = are_parentheses_valid(c["input"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")
