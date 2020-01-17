import sys

sum = 0

def get_stats(values, sum):
  if len(values) == 0:
    print ("All zeros")
    return
  values.sort()
  mean = sum / len(values)
  median = values[len(values)//2]
  mode_d = {}
  for x in values:
    mode_d[x] = mode_d.get(x, 0) + 1
  mode = max(mode_d.values())
  print (values)
  print (f"Mean is {mean}.\nMedian is {median}\nMode is {mode}\nRange is {values[0]}..{values[-1]}")


def get_inputs(values):
  global sum
  while True:
    inp = input()
    if inp.lstrip("-").isdigit():
      sum += int(inp)
      values.append(int(inp))
    elif inp == 'm':
      get_stats(values, sum)
      continue
    else:
      break

if __name__ == "__main__":
  values = []
  get_inputs(values)

