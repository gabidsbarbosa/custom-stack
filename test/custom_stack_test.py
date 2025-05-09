import pytest
from src.custom_stack_class import *

def test_stack_operations():
    stack = CustomStack(2)
    assert stack.is_empty()
    stack.push(10)
    assert not stack.is_empty()
    assert stack.top() == 10
    assert stack.pop() == 10
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_stack_full_exception():
    stack = CustomStack(1)
    stack.push(1)
    with pytest.raises(StackFullException):
        stack.push(2)

def test_top_on_empty_stack():
    stack = CustomStack(1)
    with pytest.raises(StackEmptyException):
        stack.top()
