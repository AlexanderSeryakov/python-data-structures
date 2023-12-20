import pytest

from src.linked_list import LinkedList, Node


@pytest.fixture(scope="function")
def linked_list() -> LinkedList:
    return LinkedList()


@pytest.fixture(scope="session")
def node(data: int = 1) -> Node:
    return Node(data)
