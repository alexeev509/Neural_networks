dictionary = {}
sequenceOfExceptions = []


def search_val_im_list():
    counter = 0
    for i in sequenceOfExceptions:
        answer = search(i, counter)
        if (answer != None):
            print(i)
        counter += 1


def search(inheritor, counter):
    parent = dictionary[inheritor]

    # Here we are checking if parent was in sequenceOfExceptions before current exception
    for i in range(counter):
        for j in parent:
            if (j == sequenceOfExceptions[i]):
                return parent

    if (parent == []):
        return
    for j in parent:
        return search(j, counter)


def enterInputValues():
    n = int(input())
    for i in range(n):
        inp = input().split()
        dictionary[inp[0]] = [] if (len(inp) == 1) else inp[2:]
    n = int(input())
    for i in range(n):
        sequenceOfExceptions.append(input())


enterInputValues()
search_val_im_list()
# print(dictionary)
# print(sequenceOfExceptions)
