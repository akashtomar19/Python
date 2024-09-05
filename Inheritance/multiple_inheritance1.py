# https://stackoverflow.com/questions/25372653/python-multiple-inheritance-constructor-not-called-when-using-super

class Mammal:
    def __init__(self) -> None:
        print("Mammals Constructor")
        super().__init__()
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def __init__(self) -> None:
        print("Winged Animal Constructor")
        super().__init__()
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    def __init__(self) -> None:
        super().__init__()  
    

# create an object of Bat class
b1 = Bat()

