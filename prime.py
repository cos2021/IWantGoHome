import math
f = open('primelist.txt', 'w')

def PrimeNumber(a):
    if a>3:
        A=math.sqrt(a)
        A=math.floor(A)
        A=int(A)
        for n in range(2,A+1):
         Q=a%n
         if Q!=0:
                pass

         else:
                return None
    elif a == 2 or a == 3:
        pass
    elif a <= 1:
        return None
    str_a=str(a)+"\n"
    return f.write(str_a)
        #print(a, "its prime number")





for i in range(100000):
    PrimeNumber(i)