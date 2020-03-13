n = int(input())
listGet = []
listCreateAndAdd = []
dictionary = {}
dictionary["global"] = [[None], []]
queue = []


# def create(namesp, arg):
#     queue = []
#     queue.append("global")
#     while (queue.__len__() > 0):
#         if (arg == queue[0]):
#             dictionary[queue[0]][0].append(namesp)
#             # Creating new node of dictionary
#             dictionary[namesp] = [[], []]
#             break
#         else:
#             for j in dictionary[queue[0]][0]:
#                 queue.append(j)
#             queue.pop(0)

def create(namesp, arg):
    queue = []
    for u in dictionary.keys():
        queue.append(u)

    while (queue.__len__() > 0):
        if (arg == queue[0]):
            dictionary[namesp] = [[queue[0]], []]
            break
        queue.pop(0)


def search(searchValue):
    startValue = dictionary[searchValue[1]]
    if (searchValue[2] in startValue[1]):
        return searchValue[1]
    else:
        current = searchValue[1]
        parent = dictionary[current][0]
        while (parent[0] != None):
            if (searchValue[2] in dictionary[parent[0]][1]):
                return parent[0]
            else:
                current = parent[0]
                parent = dictionary[current][0]
    return


for i in range(n):
    cmd, namesp, arg = input().split()
    if (cmd == "get"):
        listGet.append(list([cmd, namesp, arg]))
    elif (cmd == "add"):
        dictionary[namesp][1].append(arg)
    else:
        create(namesp, arg)

# print(dictionary)
# print(listGet)

for i in listGet:
    print(search(i))
