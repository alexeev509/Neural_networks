class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.countOfMoney = 0

    def can_add(self, v):
        if (v + self.countOfMoney <= self.capacity):
            return True
        else:
            return False

    def add(self, v):
        self.countOfMoney += v


class Buffer:
    def __init__(self):
        self.bufferSize = 5
        self.buffer = []

    def add(self, *a):
        for j in a:
            self.buffer.append(j)
            if (self.buffer.__len__() == self.bufferSize):
                summ = 0
                for q in self.buffer:
                    summ += q
                print(summ)
                self.buffer = []

    def get_current_part(self):
        return self.buffer


buf = Buffer()

buf.add(1, 2, 3)
print(buf.get_current_part())
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part())
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part())

buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part())
