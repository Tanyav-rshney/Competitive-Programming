#given an integer n count howmany set bit are there in n

def set_bits(n):
    count = 0
    while n:
        count += n & 1  
        n >>= 1        
    return count


n = int(input())
print(set_bits(n))  
   