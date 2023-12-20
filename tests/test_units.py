from src.linked_list import LinkedListIterator, Node


class TestLinkedList:
    def test_empty_list(self, linked_list):
        empty_linked_list = linked_list

        assert empty_linked_list.head is None
        assert empty_linked_list.head == empty_linked_list.tail

    def test_append_node(self, linked_list):
        empty_linked_list = linked_list
        once_node = Node(10)
        result = empty_linked_list.append(once_node)

        assert result is once_node
        assert empty_linked_list.head is once_node

    def test_linked_list_iter(self, linked_list):
        current_linked_list = linked_list
        nodes_count = 10

        for i in range(nodes_count):
            current_linked_list.append(Node(i))

        current_node_data = 0
        for node in current_linked_list:
            assert node.data == current_node_data
            current_node_data += 1
            assert current_node_data <= nodes_count


class TestLinkedListIterator:
    def test_iterator(self, linked_list):
        it = iter(linked_list)

        for _ in it:
            assert _
        assert isinstance(it, LinkedListIterator)
