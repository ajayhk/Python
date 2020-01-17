class CountN:
  def __init__(self, count):
    self.count = count
    self.current = 1
    return None

  def __iter__(self):
    self.current = 0
    return self

  def __next__(self):
    self.current += 1
    if self.current > self.count:
      raise StopIteration
    else:
      return self.current


if __name__ == '__main__':
  myCount = CountN(11)
  myIter = iter(myCount)
  for x in myIter:
    print (x)

  # Calling next again will cause the StopIteration to get triggered
  # print (next(myIter))
  # print (next(myIter))




