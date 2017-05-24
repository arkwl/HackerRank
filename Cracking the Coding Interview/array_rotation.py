def array_left_rotation(a, n, k):    
    array = a
    if(n < 2):
        return array
    while(k > 0):
        last = array[n-1] #last element
        tmp = 0;
        for x in range(0, n):
            #print(str(x)+"    "+str(n))
            index = abs(x - n)
            #print(str(index))
            tmp = array[index - 1]
            #print("last: " +str(last)+"temp: "+str(tmp)+" index: "+ str(index))
            array[index - 1] = last
            last = tmp
            if(index - 1 == 0):
                # copy last to n
                array[n-1]= last
                break;
        k = k - 1;
    return array

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')