class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def pop(self):
        if self.is_empty() is True:
            return False
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)



def par_check(str):
    s = Stack()
    index = 0
    for i in str:
        if i == '(':
            s.push(i)
            index += 1
        elif i == ')':
            if s.is_empty() is True:
                return False
            s.pop()
            index -= 1

    return s.is_empty()




if __name__ == '__main__':
    str1 = '(hello))'
    str2 = '(())'
    str3 = '()))(('
    str4 = '(nihao(hello))'

    print(par_check(str1))
    print(par_check(str2))
    print(par_check(str3))
    print(par_check(str4))