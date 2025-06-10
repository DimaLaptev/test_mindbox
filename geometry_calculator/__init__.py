"""
Geometry Calculator - Библиотека для вычисления площадей геометрических фигур

Поддерживаемые функции:
- circle_area: Вычисление площади круга по радиусу
- triangle_area: Вычисление площади треугольника по трем сторонам
"""

from .shapes import circle_area, triangle_area

__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "Библиотека для вычисления площадей геометрических фигур"

__all__ = ['circle_area', 'triangle_area'] 