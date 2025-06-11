"""
Тесты для модуля shapes.
"""

import unittest
import math
from geometry_calculator.shapes import (
    # Классы
    Shape, Circle, Triangle,
    # Функции
    calculate_area, is_right_triangle,
    # Legacy функции
    circle_area, triangle_area
)


class TestCircleClass(unittest.TestCase):
    """Тесты для класса Circle."""
    
    def test_circle_creation_valid(self):
        """Тест создания валидного круга."""
        circle = Circle(5)
        self.assertEqual(circle.radius, 5)
    
    def test_circle_area_calculation(self):
        """Тест вычисления площади круга."""
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), math.pi, places=7)
        
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 25 * math.pi, places=7)
        
        circle = Circle(0)
        self.assertAlmostEqual(circle.area(), 0, places=7)
    
    def test_circle_negative_radius(self):
        """Тест обработки отрицательного радиуса."""
        with self.assertRaises(ValueError):
            Circle(-1)
        with self.assertRaises(ValueError):
            Circle(-5.5)
    
    def test_circle_invalid_type_radius(self):
        """Тест обработки невалидного типа радиуса."""
        with self.assertRaises(TypeError):
            Circle("5")
        with self.assertRaises(TypeError):
            Circle(None)
        with self.assertRaises(TypeError):
            Circle([5])
    
    def test_circle_string_representation(self):
        """Тест строкового представления круга."""
        circle = Circle(5)
        self.assertEqual(str(circle), "Круг(радиус=5)")
        self.assertEqual(repr(circle), "Circle(radius=5)")


class TestTriangleClass(unittest.TestCase):
    """Тесты для класса Triangle."""
    
    def test_triangle_creation_valid(self):
        """Тест создания валидного треугольника."""
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.side_a, 3)
        self.assertEqual(triangle.side_b, 4)
        self.assertEqual(triangle.side_c, 5)
    
    def test_triangle_area_calculation(self):
        """Тест вычисления площади треугольника."""
        # Прямоугольный треугольник 3-4-5
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=7)
        
        # Равносторонний треугольник
        triangle = Triangle(6, 6, 6)
        expected_area = (math.sqrt(3) / 4) * 36
        self.assertAlmostEqual(triangle.area(), expected_area, places=7)
        
        # Произвольный треугольник
        triangle = Triangle(5, 6, 7)
        self.assertAlmostEqual(triangle.area(), 14.696938456699069, places=7)
    
    def test_triangle_is_right_triangle(self):
        """Тест проверки прямоугольного треугольника."""
        # Прямоугольные треугольники
        self.assertTrue(Triangle(3, 4, 5).is_right_triangle())
        self.assertTrue(Triangle(5, 4, 3).is_right_triangle())  # Порядок не важен
        self.assertTrue(Triangle(5, 12, 13).is_right_triangle())
        self.assertTrue(Triangle(8, 6, 10).is_right_triangle())
        
        # Непрямоугольные треугольники
        self.assertFalse(Triangle(5, 5, 5).is_right_triangle())  # Равносторонний
        self.assertFalse(Triangle(2, 3, 4).is_right_triangle())  # Произвольный
        self.assertFalse(Triangle(1, 1, 1).is_right_triangle())  # Маленький равносторонний
    
    def test_triangle_invalid_triangle(self):
        """Тест обработки сторон, не образующих треугольник."""
        with self.assertRaises(ValueError):
            Triangle(1, 2, 5)  # 1 + 2 <= 5
        with self.assertRaises(ValueError):
            Triangle(10, 1, 1)  # 1 + 1 <= 10
        with self.assertRaises(ValueError):
            Triangle(1, 10, 1)  # 1 + 1 <= 10
    
    def test_triangle_negative_sides(self):
        """Тест обработки отрицательных сторон."""
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 3)
        with self.assertRaises(ValueError):
            Triangle(1, -2, 3)
        with self.assertRaises(ValueError):
            Triangle(1, 2, -3)
    
    def test_triangle_zero_sides(self):
        """Тест обработки нулевых сторон."""
        with self.assertRaises(ValueError):
            Triangle(0, 2, 3)
        with self.assertRaises(ValueError):
            Triangle(1, 0, 3)
        with self.assertRaises(ValueError):
            Triangle(1, 2, 0)
    
    def test_triangle_invalid_type_sides(self):
        """Тест обработки невалидных типов сторон."""
        with self.assertRaises(TypeError):
            Triangle("3", 4, 5)
        with self.assertRaises(TypeError):
            Triangle(3, "4", 5)
        with self.assertRaises(TypeError):
            Triangle(3, 4, "5")
        with self.assertRaises(TypeError):
            Triangle(None, 4, 5)
    
    def test_triangle_string_representation(self):
        """Тест строкового представления треугольника."""
        triangle = Triangle(3, 4, 5)
        self.assertEqual(str(triangle), "Треугольник(стороны=3, 4, 5)")
        self.assertEqual(repr(triangle), "Triangle(side_a=3, side_b=4, side_c=5)")


class TestPolymorphicFunctions(unittest.TestCase):
    """Тесты для полиморфных функций."""
    
    def test_calculate_area_circle(self):
        """Тест полиморфного вычисления площади круга."""
        circle = Circle(5)
        area = calculate_area(circle)
        self.assertAlmostEqual(area, 25 * math.pi, places=7)
    
    def test_calculate_area_triangle(self):
        """Тест полиморфного вычисления площади треугольника."""
        triangle = Triangle(3, 4, 5)
        area = calculate_area(triangle)
        self.assertAlmostEqual(area, 6.0, places=7)
    
    def test_calculate_area_invalid_type(self):
        """Тест обработки невалидного типа в calculate_area."""
        with self.assertRaises(TypeError):
            calculate_area("not a shape")
        with self.assertRaises(TypeError):
            calculate_area(5)
        with self.assertRaises(TypeError):
            calculate_area(None)
    
    def test_is_right_triangle_function(self):
        """Тест функции is_right_triangle."""
        # Прямоугольные треугольники
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertTrue(is_right_triangle(5, 4, 3))  # Порядок не важен
        self.assertTrue(is_right_triangle(5, 12, 13))
        self.assertTrue(is_right_triangle(8, 6, 10))
        
        # Непрямоугольные треугольники
        self.assertFalse(is_right_triangle(5, 5, 5))
        self.assertFalse(is_right_triangle(2, 3, 4))
        self.assertFalse(is_right_triangle(1, 1, 1))
    
    def test_is_right_triangle_invalid_input(self):
        """Тест обработки невалидного ввода в is_right_triangle."""
        with self.assertRaises(ValueError):
            is_right_triangle(1, 2, 5)  # Невалидный треугольник
        with self.assertRaises(ValueError):
            is_right_triangle(-1, 2, 3)  # Отрицательная сторона
        with self.assertRaises(TypeError):
            is_right_triangle("3", 4, 5)  # Неправильный тип


# Тесты для обратной совместимости (Legacy Functions)
class TestCircleArea(unittest.TestCase):
    """Тесты для legacy функции circle_area."""
    
    def test_valid_radius(self):
        """Тест вычисления площади круга для валидных радиусов."""
        self.assertAlmostEqual(circle_area(1), math.pi, places=7)
        self.assertAlmostEqual(circle_area(5), 25 * math.pi, places=7)
        self.assertAlmostEqual(circle_area(0), 0, places=7)
        self.assertAlmostEqual(circle_area(2.5), 6.25 * math.pi, places=7)
    
    def test_negative_radius(self):
        """Тест обработки отрицательного радиуса."""
        with self.assertRaises(ValueError):
            circle_area(-1)
        with self.assertRaises(ValueError):
            circle_area(-5.5)
    
    def test_invalid_type_radius(self):
        """Тест обработки невалидного типа радиуса."""
        with self.assertRaises(TypeError):
            circle_area("5")
        with self.assertRaises(TypeError):
            circle_area(None)
        with self.assertRaises(TypeError):
            circle_area([5])


class TestTriangleArea(unittest.TestCase):
    """Тесты для legacy функции triangle_area."""
    
    def test_valid_triangle(self):
        """Тест вычисления площади треугольника для валидных сторон."""
        # Прямоугольный треугольник 3-4-5
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.0, places=7)
        
        # Равносторонний треугольник
        side = 6
        expected_area = (math.sqrt(3) / 4) * side ** 2
        self.assertAlmostEqual(triangle_area(side, side, side), expected_area, places=7)
        
        # Произвольный треугольник
        self.assertAlmostEqual(triangle_area(5, 6, 7), 14.696938456699069, places=7)
    
    def test_invalid_triangle(self):
        """Тест обработки сторон, не образующих треугольник."""
        with self.assertRaises(ValueError):
            triangle_area(1, 2, 5)  # 1 + 2 <= 5
        with self.assertRaises(ValueError):
            triangle_area(10, 1, 1)  # 1 + 1 <= 10
        with self.assertRaises(ValueError):
            triangle_area(1, 10, 1)  # 1 + 1 <= 10
    
    def test_negative_sides(self):
        """Тест обработки отрицательных сторон."""
        with self.assertRaises(ValueError):
            triangle_area(-1, 2, 3)
        with self.assertRaises(ValueError):
            triangle_area(1, -2, 3)
        with self.assertRaises(ValueError):
            triangle_area(1, 2, -3)
    
    def test_zero_sides(self):
        """Тест обработки нулевых сторон."""
        with self.assertRaises(ValueError):
            triangle_area(0, 2, 3)
        with self.assertRaises(ValueError):
            triangle_area(1, 0, 3)
        with self.assertRaises(ValueError):
            triangle_area(1, 2, 0)
    
    def test_invalid_type_sides(self):
        """Тест обработки невалидных типов сторон."""
        with self.assertRaises(TypeError):
            triangle_area("3", 4, 5)
        with self.assertRaises(TypeError):
            triangle_area(3, "4", 5)
        with self.assertRaises(TypeError):
            triangle_area(3, 4, "5")
        with self.assertRaises(TypeError):
            triangle_area(None, 4, 5)


if __name__ == '__main__':
    unittest.main() 