n=("abc",45)
print(n)
print(n[0])
print(len(n))
y=list(n)
y[1]="banana"
n=tuple(y)
print(n)
x=("red",)
n=n+x
print(n)
a=list(n)
a.remove("abc")
n=tuple(a)
print(n)
x,y=n
print(x)
print(y)
for item in n:
    print(item)
t=("anu",54,"rose")
for i in range(len(t)):
    print(t[i])
