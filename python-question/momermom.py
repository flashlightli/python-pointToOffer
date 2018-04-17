class A():
    name = 'A'
class B():
    name = 'B'
class C(A,B):
    pass

print(C.name)
C.name='C'
print(A.name)
print(B.name)
print(C.name)