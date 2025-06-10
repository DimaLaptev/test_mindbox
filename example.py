#!/usr/bin/env python3
"""
Примеры использования библиотеки geometry_calculator.
"""

from geometry_calculator import circle_area, triangle_area


def main():
    """Демонстрация функций библиотеки."""
    
    print("=== Geometry Calculator - Примеры использования ===\n")
    
    # Примеры вычисления площади круга
    print("1. Вычисление площади круга:")
    print("-" * 40)
    
    radii = [1, 2.5, 5, 10]
    for radius in radii:
        area = circle_area(radius)
        print(f"Радиус: {radius:4} → Площадь: {area:12.6f}")
    
    print("\n2. Вычисление площади треугольника:")
    print("-" * 40)
    
    # Примеры треугольников
    triangles = [
        (3, 4, 5),      # Прямоугольный треугольник
        (5, 5, 5),      # Равносторонний треугольник
        (5, 6, 7),      # Произвольный треугольник
        (13, 14, 15),   # Большой треугольник
    ]
    
    for a, b, c in triangles:
        area = triangle_area(a, b, c)
        print(f"Стороны: {a:2}, {b:2}, {c:2} → Площадь: {area:12.6f}")
    
    print("\n3. Обработка ошибок:")
    print("-" * 40)
    
    # Демонстрация обработки ошибок
    error_cases = [
        ("Отрицательный радиус круга", lambda: circle_area(-5)),
        ("Невалидный треугольник", lambda: triangle_area(1, 2, 5)),
        ("Нулевая сторона треугольника", lambda: triangle_area(0, 4, 5)),
        ("Неправильный тип данных", lambda: circle_area("пять")),
    ]
    
    for description, func in error_cases:
        try:
            result = func()
            print(f"{description}: ОШИБКА - не было исключения!")
        except (ValueError, TypeError) as e:
            print(f"{description}: {e}")
    
    print("\n=== Демонстрация завершена ===")


if __name__ == "__main__":
    main() 