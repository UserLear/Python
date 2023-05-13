#DUCK TYPING EN PYTHON
#.......definicion de una clase
class Pato:
    def hablar(self):
        print("¡Cua!, Cua!")

#llamamos al metodo 
p = Pato()
p.hablar()
# ¡Cua!, Cua

#definimos una funcion que llame al metodo del objeto que se le pase
def llama_hablar(x):
    x.hablar()

p = Pato()
llama_hablar(p)
# ¡Cua!, Cua!  

#definicion de otros objetos 
class Perro:
    def hablar(self):
        print("¡Guau, Guau!")

class Gato:
    def hablar(self):
        print("¡Miau, Miau!")

class Vaca:
    def hablar(self):
        print("¡Muuu, Muuu!")

llama_hablar(Perro())
llama_hablar(Gato())
llama_hablar(Vaca())

# ¡Guau, Guau!
# ¡Miau, Miau!
# ¡Muuu, Muuu

lista = [Perro(), Gato(), Vaca()]
for animal in lista:
    animal.hablar()

# ¡Guau, Guau!
# ¡Miau, Miau!
# ¡Muuu, Muuu!

#.......len()
class Foo():
    def __len__(self):
        return 99
    
class Bar():
    pass

print(len(Foo())) # 99
print(len(Bar())) # Error

