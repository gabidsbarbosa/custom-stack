import pytest
from src.number_asc_order import NumberAscOrder
from src.custom_stack_class import *


def test_sort_stack_numbers_with_mock(mocker):
    mock_stack = mocker.Mock()

    # Corrigido: mais um False para garantir todas as chamadas a pop
    mock_stack.is_empty.side_effect = [False] * 7 + [True]
    mock_stack.pop.side_effect = [1, 18, 25, 3, 7, 12]

    result = NumberAscOrder().sort(mock_stack)
    assert result == [1, 3, 7, 12, 18, 25]


def test_sort_empty_stack_with_mock(mocker):
    mock_stack = mocker.Mock()
    mock_stack.is_empty.return_value = True
    result = NumberAscOrder().sort(mock_stack)
    assert result == []
