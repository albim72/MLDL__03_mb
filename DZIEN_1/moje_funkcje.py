print("pisanie funkcji")
n=100
def policz(a:int,b:float,c:float,y:int=9)->float:
    global n
    n = (a+b)*y - c + n
    return n

print(policz(4,6.4,3.8,7))
print(policz(12,78,True))
print(n)
