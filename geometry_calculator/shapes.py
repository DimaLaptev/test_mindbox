"""
Модуль для вычисления площадей различных геометрических фигур.
"""

import math


def circle_area(radius):
    """
    Вычисляет площадь круга по радиусу.
    
    Args:
        radius (float): Радиус круга. Должен быть положительным числом.
    
    Returns:
        float: Площадь круга.
    
    Raises:
        ValueError: Если радиус не является положительным числом.
        TypeError: Если радиус не является числом.
    
    Examples:
        >>> circle_area(5)
        78.53981633974483
        >>> circle_area(0)
        0.0
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Радиус должен быть числом")
    
    if radius < 0:
        raise ValueError("Радиус должен быть неотрицательным числом")
    
    return math.pi * radius ** 2


def triangle_area(side_a, side_b, side_c):
    """
    Вычисляет площадь треугольника по трем сторонам, используя формулу Герона.
    
    Args:
        side_a (float): Длина первой стороны треугольника.
        side_b (float): Длина второй стороны треугольника.
        side_c (float): Длина третьей стороны треугольника.
    
    Returns:
        float: Площадь треугольника.
    
    Raises:
        ValueError: Если стороны не образуют валидный треугольник или являются неположительными.
        TypeError: Если стороны не являются числами.
    
    Examples:
        >>> triangle_area(3, 4, 5)
        6.0
        >>> triangle_area(5, 5, 5)
        10.825317547305483
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
    
    # Вычисление площади по формуле Герона
    semi_perimeter = (side_a + side_b + side_c) / 2
    area = math.sqrt(semi_perimeter * 
                     (semi_perimeter - side_a) * 
                     (semi_perimeter - side_b) * 
                     (semi_perimeter - side_c))
    
    return area 