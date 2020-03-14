dictionary = {}
list = []
list_of_answers = []


class question:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child


def enterInputValues():
    n = int(input())
    for i in range(n):
        class_description = input().split()
        class_name = class_description[0]
        class_parents = class_description[2:]
        dictionary[class_name] = class_parents
    q = int(input())
    for i in range(q):
        ques = input().split()
        parent = ques[0]
        child = ques[1]
        list.append(question(parent, child))


def searchParent(node, current):
    if (current not in dictionary.keys()):
        return
    parentsOfCurrentNode = dictionary[current]
    if (parentsOfCurrentNode.__len__() == 0):
        return
    for n in parentsOfCurrentNode:
        if (n == node.parent):
            return n
        else:
            result = searchParent(node, n)
            if (result == node.parent):
                return result


def search_parents_of_classes():
    for node in list:
        # BidloKod :)
        if (searchParent(node, node.child) != None or (node.parent == node.child and node.parent in dictionary.keys())):
            list_of_answers.append("Yes")
        else:
            list_of_answers.append("No")
    return list_of_answers


def print_result():
    for answer in list_of_answers:
        print(answer)

# enterInputValues()
# print(dictionary)
# search_parents_of_classes()
# print_result()
