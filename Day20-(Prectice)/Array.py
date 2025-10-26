from array import array
arr = array('i', [1, 2, 3, 4])
print(arr[2])
arr.append(5)
arr.insert(1, 10)
arr.remove(3)
print(arr[1:3])






matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in matrix:
    print(row)
