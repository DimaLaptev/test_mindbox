"""
Тесты для модуля shapes.
"""

import unittest
import math
from geometry_calculator.shapes import circle_area, triangle_area


class TestCircleArea(unittest.TestCase):
    """Тесты для функции circle_area."""
    
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
    """Тесты для функции triangle_area."""
    
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