#!/usr/bin/env python3
"""
Примеры использования библиотеки geometry_calculator.
Демонстрация новых возможностей: классы, полиморфизм, проверка прямоугольного треугольника.
"""

from geometry_calculator import (
    # Классы фигур
    Circle, Triangle,
    # Полиморфные функции
    calculate_area, is_right_triangle,
    # Legacy функции
    circle_area, triangle_area
)


def main():
    """Демонстрация функций библиотеки."""
    
    print("=== Geometry Calculator v2.0 - Примеры использования ===\n")
    
    # 1. Демонстрация классов фигур
    print("1. Работа с классами фигур:")
    print("-" * 50)
    
    # Создание фигур
    circle = Circle(5)
    triangle = Triangle(3, 4, 5)
    big_circle = Circle(10)
    equilateral_triangle = Triangle(6, 6, 6)
    
    print(f"Круг: {circle}")
    print(f"Площадь: {circle.area():.6f}")
    print()
    
    print(f"Треугольник: {triangle}")
    print(f"Площадь: {triangle.area():.6f}")
    print(f"Прямоугольный: {triangle.is_right_triangle()}")
    print()
    
    # 2. Полиморфное вычисление площади
    print("2. Полиморфное вычисление площади:")
    print("-" * 50)
    
    shapes = [circle, triangle, big_circle, equilateral_triangle]
    
    for shape in shapes:
        area = calculate_area(shape)  # Одна функция для всех фигур!
        print(f"{shape} → Площадь: {area:.6f}")
    
    print("\n🎯 Главное преимущество: одна функция calculate_area() работает")
    print("   с любыми фигурами без знания их типа в compile-time!\n")
    
    # 3. Проверка прямоугольных треугольников
    print("3. Проверка прямоугольных треугольников:")
    print("-" * 50)
    
    test_triangles = [
        (3, 4, 5),       # Классический прямоугольный
        (5, 12, 13),     # Еще один прямоугольный
        (8, 6, 10),      # Прямоугольный (порядок сторон другой)
        (5, 5, 5),       # Равносторонний (не прямоугольный)
        (2, 3, 4),       # Произвольный (не прямоугольный)
        (1, 1, 1.414),   # Почти прямоугольный
    ]
    
    for a, b, c in test_triangles:
        try:
            triangle = Triangle(a, b, c)
            is_right = triangle.is_right_triangle()
            
            # Также можно использовать функцию напрямую
            is_right_func = is_right_triangle(a, b, c)
            
            status = "✓ Прямоугольный" if is_right else "✗ Не прямоугольный"
            print(f"Треугольник ({a}, {b}, {c}): {status}")
            
        except ValueError as e:
            print(f"Треугольник ({a}, {b}, {c}): ❌ {e}")
    
    # 4. Легкость добавления новых фигур
    print("\n4. Легкость добавления новых фигур:")
    print("-" * 50)
    print("Для добавления новой фигуры достаточно:")
    print("1. Создать класс, наследующий от Shape")
    print("2. Реализовать методы area() и __str__()")
    print("3. Новая фигура автоматически работает с calculate_area()!")
    print("\nПример добавления прямоугольника:")
    print("""
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Прямоугольник({self.width}x{self.height})"

# И всё! Теперь можно использовать:
# rect = Rectangle(4, 6)
# area = calculate_area(rect)  # Работает автоматически!
    """)
    
    # 5. Обратная совместимость
    print("5. Обратная совместимость (legacy функции):")
    print("-" * 50)
    
    print("Старый API продолжает работать:")
    old_circle_area = circle_area(5)
    old_triangle_area = triangle_area(3, 4, 5)
    
    print(f"circle_area(5) = {old_circle_area:.6f}")
    print(f"triangle_area(3, 4, 5) = {old_triangle_area:.6f}")
    print("(Рекомендуется переходить на новый API с классами)")
    
    # 6. Обработка ошибок
    print("\n6. Обработка ошибок:")
    print("-" * 50)
    
    error_cases = [
        ("Отрицательный радиус", lambda: Circle(-5)),
        ("Невалидный треугольник", lambda: Triangle(1, 2, 5)),
        ("Полиморфизм с неправильным типом", lambda: calculate_area("не фигура")),
        ("Проверка прямоугольности невалидного треугольника", lambda: is_right_triangle(1, 1, 5)),
    ]
    
    for description, func in error_cases:
        try:
            result = func()
            print(f"{description}: ОШИБКА - не было исключения!")
        except (ValueError, TypeError) as e:
            print(f"{description}: {e}")
    
    print("\n=== Все требования выполнены! ===")
    print("✅ Легкость добавления других фигур")
    print("✅ Вычисление площади без знания типа в compile-time")
    print("✅ Проверка прямоугольного треугольника")
    print("✅ Обратная совместимость")


if __name__ == "__main__":
    main() 