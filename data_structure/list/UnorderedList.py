class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        assert type(new_next) is Node, "The type is not Node"
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_item = Node(data)
        new_item.next = self.head
        self.head = new_item
        self.size += 1

    def remove(self, data):
        assert self.is_empty() == False, "No available item to delete"
        temp = self.head
        previous = None
        found = False
        while temp:
            if temp.get_data() == data:
                found = True
                break
            elif temp is None:
                break
            else:
                previous = temp
                temp = temp.get_next()
        if previous is None and found == True:
            self.head = temp.get_next()
        elif found is True:
            previous.set_next(temp.get_next())
        else:
            print("Item not found")


# temp = Node(15)
# temp.next = Node(20)
# print(temp.get_data())
# print(temp.next.get_data())

# if __name__ == '__main__':
#     myList = UnorderedList()
#     for i in range(1, 11):
#         myList.add(i)
#
#     myList.remove(7)
#
#     temp = myList.head
#     for i in range(6):
#         print(temp.data)
#         temp = temp.get_next()

