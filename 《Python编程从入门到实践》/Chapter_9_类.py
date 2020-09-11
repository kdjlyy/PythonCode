# 第九章 类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('wille', '6')
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + my_dog.age + " years old.")
my_dog.sit()
my_dog.roll_over()
# My dog's name is Wille.
# My dog is 6 years old.
# Wille is now sitting.
# Wille rolled over!


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car("Audi", "A4", 2016)
print(my_new_car.get_descriptive_name())  # 2016 Audi A4
my_new_car.read_odometer()  # This car has 0 miles on it.
# 修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()  # This car has 23 miles on it.

my_new_car.update_odometer(99)
my_new_car.read_odometer()  # This car has 99 miles on it.

my_new_car.increment_odometer(100)
my_new_car.read_odometer()  # This car has 199 miles on it.

# 类的继承


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        """父类也成为超类(superclass),super以此得名，这行代码让Python调用ElectricCar的父类的方法__init__()，让ElectricCar类包含父类的所有属性"""

        """子类的独特之处"""
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " KWh battery.")


my_eCar = ElectricCar("Tesla", "model s", 2016)
print(my_eCar.get_descriptive_name())  # 2016 Tesla Model S
my_eCar.describe_battery()  # This car has a 70 KWh battery.

# 将实例用作属性
#  (这里将一个Battery实例用作ElectricCar类的一个属性)


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " KWh battery.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        """父类也成为超类(superclass),super以此得名，这行代码让Python调用ElectricCar的父类的方法__init__()，让ElectricCar类包含父类的所有属性"""

        """子类的独特之处"""
        self.battery = Battery()

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " KWh battery.")


my_Tesla = ElectricCar("Tesla", "Model S", 2020)
my_Tesla.battery.describe_battery()  # This car has a 70 KWh battery.

# Python标准库举例(模块collections中的OrderedDict类，记录了键值对的添加顺序)
from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['jen'] = 'python'
favorite_language['sarah'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'

for name, language in favorite_language.items():
    print(name.title() + " 's favorite language is " + language.title())
# Jen 's favorite language is Python
# Sarah 's favorite language is C
# Edward 's favorite language is Ruby
# Phil 's favorite language is Python

