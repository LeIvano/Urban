class Figure:
    def __init__(self, color: tuple, *sides, filled=True, sides_count=0):
        self.sides_count = sides_count
        self.__color = color

        if self.__is_valid_sides(*sides) or sides_count == 12:
            self.__sides = list(sides)[0]
        else:
            self.__sides = self.__make_one_sided()
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *color):
        if isinstance(color, tuple):
            if len(color) != 3:
                return False
        else:
            return False

        if 0 <= color[0] <= 255 and 0 <= color[1] <= 255 and 0 <= color[2] <= 255:
            return True
        else:
            return False

    def set_color(self, *color):
        if self.__is_valid_color(*color):
            self.__color = color

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False

        for side in new_sides:
            if side <= 0:
                return False

        return True

    def __make_one_sided(self):
        return [1 for _ in range(self.sides_count)]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides, sides_count=1)
        self.__radius = sides[0] / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides, sides_count=3)

    def get_square(self):
        a = self.__sides[0]
        b = self.__sides[1]
        c = self.__sides[2]
        p = 0.5 * (a + b + c)

        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    def __init__(self, color, sides):
        sides = [sides for _ in range(12)]
        super().__init__(color, sides, sides_count=12)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
