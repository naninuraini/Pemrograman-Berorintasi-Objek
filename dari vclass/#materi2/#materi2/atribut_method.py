#class atribut
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John", 25)
person2 = Person("Nani", 20)

print(person1.name)
print(person2.age)

#class method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

person1 = Person("John", 25)
person1.greeting()


#Atribut dan metode kelas
class Car:
    # class attribute
    brand = "Toyota"

    def __init__(self, model, year):
        self.model = model
        self.year = year

    # class method
    @classmethod
    def change_brand(cls, new_brand):
        cls.brand = new_brand

# create objects
car1 = Car("Corolla", 2022)
car2 = Car("Camry", 2021)

# access class attribute
print(car1.brand)  # output: Toyota
print(car2.brand)  # output: Toyota

# access and change class attribute
print(Car.brand)  # output: Toyota
Car.change_brand("Honda")
print(Car.brand)  # output: Honda
print(car1.brand)  # output: Honda
print(car2.brand)  # output: Honda


#Intance atribut dan metode objek
#Intance atribut
class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

mobil1 = Mobil('Toyota', 'Merah')
mobil2 = Mobil('Honda', 'Hitam')

print(mobil1.merek) 
print(mobil2.warna) 

#Intance method
class Lingkaran:

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def luas(self):
        return 3.14 * (self.jari_jari ** 2)
    
    def keliling(self):
        return 2 * 3.14 * self.jari_jari

lingkaran1 = Lingkaran(7)
lingkaran2 = Lingkaran(14)

print(lingkaran2.keliling())