xs = list(map(int, input().split()))
S = max(xs)               
xs.remove(S)              
a = S - xs[2]
b = S - xs[1]
c = S - xs[0]
print(a, b, c)
