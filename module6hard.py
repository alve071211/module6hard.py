import math


class Figure:

    sides_count = 0
    def __init__(self, color, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

        if self.__is_valid_color(*color):
            self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if not (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
            return False
        elif 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False
                #return all(isinstance[0, 255])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):  #проверка цвета на соответствие
            self.__color = [r, g, b]        #изменение цвета

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not (isinstance(side, int) and side > 0):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.sides_count = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = len(self) / (2 * math.pi)

        if len(self.get_sides()) != self.sides_count:
            self.set_sides(1)

    def get_square(self):
        math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        first, second, third = self.get_sides()
        half_of_per = sum([first, second, third]) / 2
        area = math.sqrt(half_of_per * (half_of_per - first) * (half_of_per - second) * (half_of_per - third))
        return 2 * area / first

    def get_square(self):
        first, _, _ = self.get_sides()
        return 0.5 * first * self.__height

    def get_height(self):
        return self.__height

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))

    def get_sides(self):
        return [self.__sides] * self.sides_count

    def get_volume(self):
        return (self.__sides**3)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


