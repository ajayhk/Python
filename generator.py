


class myGen(object):
  def __init__(self, n):
    self.n = n
    self.num = 1

  def __iter__(self):
    return self

  def __next__(self):
    return self.next()

  def next(self):
    if self.num <= self.n:
      cur, self.num = self.num, self.num+1
      return cur
    else:
      raise StopIteration()

sum_of_first_1000 = sum(myGen(10))
print (sum_of_first_1000)
