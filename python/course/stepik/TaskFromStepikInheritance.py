dictionary = {}
n = int(input())
list = []


class question:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child


for i in range(n):
    class_description = input().split()
    class_name = class_description[0]
    class_parents = class_description[2:]
    dictionary[class_name] = class_parents

print(dictionary)

q = int(input())

for i in range(q):
    ques = input().split()
    parent = ques[0]
    child = ques[1]
    list.append(question(parent, child))


def searchParent(node, current):
    parentsOfCurrentNode = dictionary[current]
    if (parentsOfCurrentNode.__len__() == 0):
        return
    for n in parentsOfCurrentNode:
        if (n == node.parent):
            return n
        else:
            searchParent(node, n)


for node in list:
    if (searchParent(node, node.child) != None):
        print("Yes")
    else:
        print("No")
