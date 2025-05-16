import pytest
from src.custom_stack_class import *


def test_push_and_pop_stack():
    stack = CustomStack(2)
    stack.push(5)
    stack.push(10)
    assert stack.pop() == 10
    assert stack.pop() == 5


def test_stack_overflow():
    stack = CustomStack(1)
    stack.push(1)
    with pytest.raises(StackFullException):
        stack.push(2)


def test_stack_underflow():
    stack = CustomStack(1)
    with pytest.raises(StackEmptyException):
        stack.pop()
