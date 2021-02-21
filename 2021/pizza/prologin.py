N = 10**6
m = 1300
import math

def lecool(N, m):
    a = 1
    for i in range(N, m, -1):
        a *= i
    return a

#a = 1/(N**m) * lecool(N, m)

b = 1-math.exp(-m*m/(2*N))
print(b)