class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self) -> str:
        return "Какой-то звук..."

    def display_info(self) -> None:
        print(f"[Животное] Имя: {self.name}, Возраст: {self.age} лет.")


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        return "Гав"

    def fetch_ball(self) -> None:
        print(f"{self.name} ({self.breed}) играет с мячом")


class Cat(Animal):
    def __init__(self, name: str, age: int, is_indoor: bool = True):
        super().__init__(name, age)
        self.is_indoor = is_indoor

    def make_sound(self) -> str:
        return "Мяу"

    def scratch_furniture(self) -> None:
        if self.is_indoor:
            print(f"{self.name} дерёт диван")
        else:
            print(f"{self.name} спит")


if __name__ == "__main__":
    my_dog = Dog(name="Булка", age=3, breed="Лабрадор")
    my_cat = Cat(name="Муся", age=5, is_indoor=True)
    street_cat = Cat(name="Барсик", age=2, is_indoor=False)

    animals = [my_dog, my_cat, street_cat]

    for animal in animals:
        animal.display_info()
        print(f"Говорит: {animal.make_sound()}")

        if isinstance(animal, Dog):
            animal.fetch_ball()
        elif isinstance(animal, Cat):
            animal.scratch_furniture()
        print("-" * 30)