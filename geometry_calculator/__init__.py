"""
Geometry Calculator - Библиотека для вычисления площадей геометрических фигур

Поддерживаемые функции:
- Circle, Triangle: Классы для представления фигур
- calculate_area: Полиморфное вычисление площади любой фигуры
- is_right_triangle: Проверка прямоугольного треугольника
- circle_area, triangle_area: Legacy функции (deprecated)
"""

from .shapes import (
    # Основные классы
    Shape,
    Circle,
    Triangle,
    
    # Полиморфные функции
    calculate_area,
    is_right_triangle,
    
    # Legacy функции (для обратной совместимости)
    circle_area,
    triangle_area
)

__version__ = "2.0.0"
__author__ = "Shipilov Dmitriy, shipilenok1@gmail.com"
__description__ = "Библиотека для вычисления площадей геометрических фигур с поддержкой полиморфизма"

__all__ = [
    # Основные классы
    'Shape',
    'Circle', 
    'Triangle',
    
    # Полиморфные функции
    'calculate_area',
    'is_right_triangle',
    
    # Legacy функции
    'circle_area',
    'triangle_area'
] 