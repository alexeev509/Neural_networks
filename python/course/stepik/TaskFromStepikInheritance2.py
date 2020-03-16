import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, element):
        self.log(element)
        super(LoggableList, self).append(element)


a = LoggableList()
a.append(5)
print(a)


class ExtendedStack(list):
    def sum(self):
        if (self.__len__() > 1):
            self.append(self.pop() + self.pop())

    def sub(self):
        if (self.__len__() > 1):
            self.append(self.pop() - self.pop())

    def mul(self):
        if (self.__len__() > 1):
            self.append(self.pop() * self.pop())

    def div(self):
        if (self.__len__() > 1):
            self.append(self.pop() / self.pop())


class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if (x < 0):
            raise NonPositiveError("Error")
        else:
            super(PositiveList, self).append(x)
