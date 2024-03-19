#przykład 1 - funkcja

print("pisanie funkcji")
n=100
def policz(a:int,b:float,c:float,y:int=9)->float:
    global n
    n = (a+b)*y - c + n
    return n

print(policz(4,6.4,3.8,7))
print(policz(12,78,True))
print(n)

#przykład 2 - funkcje anonimowe

print((lambda a:a+16)(15))
s = lambda a,b,z:(a*b-2*z)/(a+b+z)

print(s(2,5,8))

num = [56,5,21,8,-9,0,21,3,123,15,67,88,90,-34,-101,8,7]
#utwórz nową listę nbparz i przekaż do niej elementy listy num o wartości parzystej

nbparz = list(filter(lambda x:x%2==0,num))
print(nbparz)

#utwórz nową listę cube i przekaż do niej wszystkie elementy listy num podniesione do potęgi 3

cube = list(map(lambda x:x**3,num))
print(cube)

#zastosowanie list comprehension

kwadraty = [i**2 for i in range(5,105,5)]
print(kwadraty)
