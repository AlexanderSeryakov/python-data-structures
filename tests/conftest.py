import pytest

from src.data_structures import LinkedList, Node


@pytest.fixture(scope="function")
def linked_list() -> LinkedList:
    return LinkedList()


@pytest.fixture(scope="session")
def node(data: int = 1) -> Node:
    return Node(data)
