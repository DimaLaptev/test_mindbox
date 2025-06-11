#!/usr/bin/env python3
"""
Демонстрация легкости добавления новых фигур в библиотеку geometry_calculator.
"""

import math
from geometry_calculator import Shape, calculate_area


# Пример 1: Прямоугольник
class Rectangle(Shape):
    """Прямоугольник."""
    
    def __init__(self, width: float, height: float):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Ширина и высота должны быть числами")
        
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными")
        
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def __str__(self) -> str:
        return f"Прямоугольник({self.width}x{self.height})"


# Пример 2: Правильный шестиугольник
class RegularHexagon(Shape):
    """Правильный шестиугольник."""
    
    def __init__(self, side_length: float):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Длина стороны должна быть числом")
        
        if side_length <= 0:
            raise ValueError("Длина стороны должна быть положительной")
        
        self.side_length = side_length
    
    def area(self) -> float:
        # Площадь правильного шестиугольника: (3√3/2) * a²
        return (3 * math.sqrt(3) / 2) * self.side_length ** 2
    
    def __str__(self) -> str:
        return f"Правильный шестиугольник(сторона={self.side_length})"


# Пример 3: Эллипс
class Ellipse(Shape):
    """Эллипс."""
    
    def __init__(self, semi_major_axis: float, semi_minor_axis: float):
        if not isinstance(semi_major_axis, (int, float)) or not isinstance(semi_minor_axis, (int, float)):
            raise TypeError("Полуоси должны быть числами")
        
        if semi_major_axis <= 0 or semi_minor_axis <= 0:
            raise ValueError("Полуоси должны быть положительными")
        
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis
    
    def area(self) -> float:
        # Площадь эллипса: π * a * b
        return math.pi * self.semi_major_axis * self.semi_minor_axis
    
    def __str__(self) -> str:
        return f"Эллипс(a={self.semi_major_axis}, b={self.semi_minor_axis})"


def main():
    """Демонстрация расширяемости библиотеки."""
    
    print("=== Демонстрация легкости добавления новых фигур ===\n")
    
    # Создание различных фигур
    shapes = [
        Rectangle(4, 6),
        RegularHexagon(5),
        Ellipse(3, 4),
        Rectangle(2.5, 8),
        RegularHexagon(2),
        Ellipse(5, 5),  # Это круг (a = b)
    ]
    
    print("Все фигуры работают с единой функцией calculate_area():")
    print("-" * 60)
    
    total_area = 0
    for i, shape in enumerate(shapes, 1):
        area = calculate_area(shape)  # Полиморфизм в действии!
        total_area += area
        print(f"{i}. {shape}")
        print(f"   Площадь: {area:.6f}")
        print()
    
    print(f"Общая площадь всех фигур: {total_area:.6f}")
    
    print("\n" + "=" * 60)
    print("🎯 Ключевые преимущества новой архитектуры:")
    print("✅ Добавление новой фигуры = всего лишь один новый класс")
    print("✅ Автоматическая поддержка полиморфизма")
    print("✅ Единообразный интерфейс для всех фигур")
    print("✅ Легкость тестирования и сопровождения")
    print("✅ Соблюдение принципов SOLID")


if __name__ == "__main__":
    main() 