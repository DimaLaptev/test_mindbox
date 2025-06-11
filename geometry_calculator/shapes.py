"""
Модуль для вычисления площадей различных геометрических фигур.
Поддерживает полиморфизм и легкое добавление новых фигур.
"""

import math
from abc import ABC, abstractmethod
from typing import Protocol, Union


class Shape(ABC):
    """
    Абстрактный базовый класс для всех геометрических фигур.
    """
    
    @abstractmethod
    def area(self) -> float:
        """
        Вычисляет площадь фигуры.
        
        Returns:
            float: Площадь фигуры.
        """
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление фигуры."""
        pass


class Circle(Shape):
    """
    Класс для представления круга.
    """
    
    def __init__(self, radius: float):
        """
        Инициализация круга.
        
        Args:
            radius (float): Радиус круга. Должен быть неотрицательным числом.
            
        Raises:
            ValueError: Если радиус отрицательный.
            TypeError: Если радиус не является числом.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть числом")
        
        if radius < 0:
            raise ValueError("Радиус должен быть неотрицательным числом")
        
        self.radius = radius
    
    def area(self) -> float:
        """
        Вычисляет площадь круга.
        
        Returns:
            float: Площадь круга.
        """
        return math.pi * self.radius ** 2
    
    def __str__(self) -> str:
        return f"Круг(радиус={self.radius})"
    
    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    """
    Класс для представления треугольника.
    """
    
    def __init__(self, side_a: float, side_b: float, side_c: float):
        """
        Инициализация треугольника.
        
        Args:
            side_a (float): Длина первой стороны треугольника.
            side_b (float): Длина второй стороны треугольника.
            side_c (float): Длина третьей стороны треугольника.
            
        Raises:
            ValueError: Если стороны не образуют валидный треугольник или являются неположительными.
            TypeError: Если стороны не являются числами.
        """
        # Проверка типов
        for side in [side_a, side_b, side_c]:
            if not isinstance(side, (int, float)):
                raise TypeError("Все стороны должны быть числами")
        
        # Проверка положительности сторон
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Все стороны должны быть положительными числами")
        
        # Проверка неравенства треугольника
        if (side_a + side_b <= side_c or 
            side_a + side_c <= side_b or 
            side_b + side_c <= side_a):
            raise ValueError("Заданные стороны не образуют валидный треугольник")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self) -> float:
        """
        Вычисляет площадь треугольника по формуле Герона.
        
        Returns:
            float: Площадь треугольника.
        """
        # Вычисление площади по формуле Герона
        semi_perimeter = (self.side_a + self.side_b + self.side_c) / 2
        area = math.sqrt(semi_perimeter * 
                         (semi_perimeter - self.side_a) * 
                         (semi_perimeter - self.side_b) * 
                         (semi_perimeter - self.side_c))
        return area
    
    def is_right_triangle(self) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным.
        
        Использует теорему Пифагора: c² = a² + b²
        
        Returns:
            bool: True, если треугольник прямоугольный, False в противном случае.
        """
        # Сортируем стороны для удобства проверки
        sides = sorted([self.side_a, self.side_b, self.side_c])
        a, b, c = sides[0], sides[1], sides[2]  # c - гипотенуза
        
        # Проверяем теорему Пифагора с учетом погрешностей вычислений
        return abs(c**2 - (a**2 + b**2)) < 1e-10
    
    def __str__(self) -> str:
        return f"Треугольник(стороны={self.side_a}, {self.side_b}, {self.side_c})"
    
    def __repr__(self) -> str:
        return f"Triangle(side_a={self.side_a}, side_b={self.side_b}, side_c={self.side_c})"


# Полиморфная функция для вычисления площади любой фигуры
def calculate_area(shape: Shape) -> float:
    """
    Вычисляет площадь любой геометрической фигуры без знания её типа в compile-time.
    
    Args:
        shape (Shape): Экземпляр любого класса, наследующего от Shape.
        
    Returns:
        float: Площадь фигуры.
        
    Raises:
        TypeError: Если переданный объект не является фигурой.
        
    Examples:
        >>> circle = Circle(5)
        >>> calculate_area(circle)
        78.53981633974483
        
        >>> triangle = Triangle(3, 4, 5)
        >>> calculate_area(triangle)
        6.0
    """
    if not isinstance(shape, Shape):
        raise TypeError("Объект должен быть экземпляром класса Shape")
    
    return shape.area()


# Функция проверки прямоугольного треугольника
def is_right_triangle(side_a: float, side_b: float, side_c: float) -> bool:
    """
    Проверяет, является ли треугольник с заданными сторонами прямоугольным.
    
    Args:
        side_a (float): Длина первой стороны треугольника.
        side_b (float): Длина второй стороны треугольника.  
        side_c (float): Длина третьей стороны треугольника.
        
    Returns:
        bool: True, если треугольник прямоугольный, False в противном случае.
        
    Raises:
        ValueError: Если стороны не образуют валидный треугольник или являются неположительными.
        TypeError: Если стороны не являются числами.
        
    Examples:
        >>> is_right_triangle(3, 4, 5)
        True
        >>> is_right_triangle(5, 5, 5)
        False
    """
    triangle = Triangle(side_a, side_b, side_c)  # Валидация происходит в конструкторе
    return triangle.is_right_triangle()


# Совместимость с предыдущей версией API (legacy functions)
def circle_area(radius: float) -> float:
    """
    Вычисляет площадь круга по радиусу.
    
    DEPRECATED: Используйте Circle(radius).area() или calculate_area(Circle(radius))
    
    Args:
        radius (float): Радиус круга. Должен быть неотрицательным числом.
    
    Returns:
        float: Площадь круга.
    """
    circle = Circle(radius)
    return circle.area()


def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    """
    Вычисляет площадь треугольника по трем сторонам, используя формулу Герона.
    
    DEPRECATED: Используйте Triangle(side_a, side_b, side_c).area() или calculate_area(Triangle(...))
    
    Args:
        side_a (float): Длина первой стороны треугольника.
        side_b (float): Длина второй стороны треугольника.
        side_c (float): Длина третьей стороны треугольника.
    
    Returns:
        float: Площадь треугольника.
    """
    triangle = Triangle(side_a, side_b, side_c)
    return triangle.area() 