# iterator

n = [2,3,1,5,8,3]

it = iter(n)            # iter is a inbuilt funtion   - it'll iterate the value



print(it.__next__())
print(next(it))                 # next is a inbuilt function - each time it fetch next value


class top10:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num += 1
            return  val

        else:
            raise StopIteration                 # raise stop the iteration


values = top10()

for i in values:
    print(i)
