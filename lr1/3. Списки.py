# списки
import copy

numbers = [7,2,5]
numbers.append(4)
numbers.insert(1, 10)
numbers.extend([1,1,1])
numbers.remove(7)
n1 = numbers.pop()
numbers.sort()
numbers.reverse()
numbers.count(2)
d = numbers.index(1)
e = numbers.copy()
copy.deepcopy(numbers)
numbers.clear()
print(numbers, e)