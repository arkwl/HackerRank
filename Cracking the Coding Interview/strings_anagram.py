import collections
from string import ascii_lowercase

def number_needed(a, b):
    #pass both strings through hashmaps
    hashmap_a = collections.Counter(a)
    hashmap_b = collections.Counter(b)
    counter = 0
    
    for c in ascii_lowercase:
        if(hashmap_a[c] == hashmap_b[c]):
            #print("pass")
            pass
        else:
            counter = counter + abs(hashmap_a[c] - hashmap_b[c])
            #print("different: " +str(c)+ "    a: "+str(hashmap_a[c])+" b: "+str(hashmap_b[c]))
    #then compare
    return counter
    
  

a = input().strip()
b = input().strip()

print(number_needed(a, b))
