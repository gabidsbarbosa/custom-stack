from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder

def test_sort_stack_numbers():
    stack = CustomStack(6)
    for num in [12, 7, 3, 25, 18, 1]:
        stack.push(num)
    result = NumberAscOrder().sort(stack)
    assert result == [1, 3, 7, 12, 18, 25]

def test_sort_empty_stack():
    stack = CustomStack(6)
    result = NumberAscOrder().sort(stack)
    assert result == []
