class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def create_head(self, data):
        node = Node(data, self.head)
        self.head = node

    def create_next(self, data):
        if self.head is None:
            self.head = Node(data, None)
        temp = self.head
        while temp.next_node:
            temp = temp.next_node
        temp.next_node = Node(data, None)

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next_node
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next_node
        if temp is None:
            return
        prev.next_node = temp.next
        temp = None

    def reverse_node(self):
        prev = None
        temp = self.head
        while temp is not None:
            next_node = temp.next_node
            temp.next_node = prev
            prev = temp
            temp = next_node
        self.head = prev

    def delete_tail(self):
        if self.head is not None:
            if self.head.next_node is None:
                self.head = None
            else:
                temp = self.head
                while temp.next_node.next_node is not None:
                    temp = temp.next_node
        last_node = temp.next_node
        last_for_print = last_node
        temp.next_node = None
        last_node = None
        print(last_for_print.data)

    def delete_head(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next_node
            temp = None

    def search_node(self, key):
        temp = self.head

        if temp.data == key:
            print("We have found necessary item %s " % format(temp.data))
        else:
            print('Element not found')
        temp = temp.next_node

    def to_array(self):
        arr = []
        temp = self.head
        while temp is not None:
            arr.append(temp.data)
            temp = temp.next_node

        print(arr)
        return

    def from_array(self, data):
        for i in range(0, len(data), 1):
            self.create_next(data[i])
        return

    def printing_list(self):
        temp = self.head
        linked_list_str = ''
        if temp is None:
            print('List is empty')
        while temp:
            linked_list_str += '[' + str(temp.data) + '] ' + '-->'
            temp = temp.next_node
        print(linked_list_str)


if __name__ == '__main__':
    list1 = LinkedList()  # create an example of class
    # test our Linked list
    list1.create_head('two')  # add head
    list1.create_next(4)
    list1.create_next(68.6)
    list1.create_next(15)
    list1.from_array(data=[90, 80, 70])  # add from array
    list1.printing_list()  # print as string
    list1.to_array()  # convert to array
    list1.delete_tail()  # delete the last element
    list1.printing_list()
    list1.delete_head()  # delete first element
    list1.printing_list()
    list1.search_node(4)  # find Node with value
