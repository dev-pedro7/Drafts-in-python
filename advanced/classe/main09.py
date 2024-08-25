class A:
    value_a = 'Valor A'
    def metodo(self):
        print("A")

class B(A):
    value_b = 'Valor B'
    def metodo(self):
        print("B")        

class C(B):
    value_c = 'Valor C'
    def metodo(self):
        super().metodo()
        print("C")

c = C()
print(c.value_a)
print(c.value_b)
print(c.value_c)
c.metodo()