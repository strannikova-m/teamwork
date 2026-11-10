class Farm:
    def __init__(self, location="Невідомо", animals_count=0, fan_power=0,
                 number=0, name="Без назви"):
        self.__location = location
        self.__animals_count = animals_count
        self.__fan_power = fan_power
        self.number = number
        self.name = name
    def __eq__(self, other):
        return self.__animals_count == other.__animals_count
    def __gt__(self, other):
        return self.__animals_count > other.__animals_count
    def __it__(self, other):
            return self.__animals_count > other.__animals_count
    def get_location(self):
        return self.__location
    def set_location(self, new_location):
        self.__location = new_location 
    def get_animals_count(self):
        return self.__animals_count

    def get_fan_power(self):
        return self.__fan_power

    def __str__(self):
        return f"Ферма {self.name}: {self.__location}, тварин: {self.__animals_count}, вентилятори: {self.__fan_power} Вт"

    def __repr__(self):
        return f"Farm('{self.__location}', {self.__animals_count}, {self.__fan_power}, {self.number}, '{self.name}')"

    def __del__(self):
        print("Об'єкт видалено:", self.name)


def main():
    farm1 = Farm()
    farm2 = Farm("Львівська область", 150, 2500, 2, "Зоря")
    farm3 = Farm("Полтавська область", 300, 4000, 3, "Калина")

    for farm in [farm1, farm2, farm3]:
        print("Номер:", farm.number)
        print("Назва:", farm.name)
        print("Місцезнаходження:", farm.get_location())
        print("Кількість тварин:", farm.get_animals_count())
        print("Потужність вентиляторів:", farm.get_fan_power())
        print(farm)
        print(repr(farm))
        print()
  
    print(farm1.get_location())       
    farm1.set_location("Львів")
    print(farm1.get_location())


    if farm1 == farm2:
        print("тварин однакова")
    elif farm1 < farm2:
        print("На першій менше")
    else:
        print("На другій  більше")
main()

