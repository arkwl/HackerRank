def rotate(array):
    temp = array[0]
    del array[0]
    array.append(temp)
    return array

def array_left_rotation(a, n, k):
    array = a
    rotations = k % n
    for i in range(rotations):
        array = rotate(array)
    return array


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
