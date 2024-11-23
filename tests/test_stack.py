"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack

def test_node_creation():
    """Тестирование создания экземпляра Node"""
    node = Node(5, None)
    assert node.data == 5
    assert node.next_node is None

def test_stack_push_and_pop():
    """Тестирование отправки и извлечения элементов из стека"""
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    assert stack.top.data == 'data3'
    assert stack.top.next_node.data == 'data2'
    assert stack.top.next_node.next_node.data == 'data1'
    assert stack.top.next_node.next_node.next_node is None
    assert stack.pop() == 'data3'
    assert stack.top.data == 'data2'
    assert stack.pop() == 'data2'
    assert stack.top.data == 'data1'
    assert stack.pop() == 'data1'
    assert stack.top is None
    assert stack.pop() is None

def test_stack_empty():
    """Тестирование поведения стека, когда он пуст"""
    stack = Stack()
    assert stack.top is None
    assert stack.pop() is None