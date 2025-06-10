# Geometry Calculator

Библиотека для вычисления площадей геометрических фигур.

## Возможности

- Вычисление площади треугольника по трем сторонам (формула Герона)
- Вычисление площади круга по радиусу
- Валидация входных данных
- Обработка ошибок

## Установка

```bash
pip install geometry_calculator
```

Для разработки:
```bash
git clone <repository-url>
cd geometry_calculator
pip install -e .
pip install -r requirements.txt
```

## Использование

### Импорт библиотеки

```python
from geometry_calculator import circle_area, triangle_area
```

### Вычисление площади круга

```python
# Площадь круга с радиусом 5
area = circle_area(5)
print(f"Площадь круга: {area}")  # Площадь круга: 78.53981633974483
```

### Вычисление площади треугольника

```python
# Площадь треугольника со сторонами 3, 4, 5
area = triangle_area(3, 4, 5)
print(f"Площадь треугольника: {area}")  # Площадь треугольника: 6.0
```

## API Документация

### `circle_area(radius)`

Вычисляет площадь круга по радиусу.

**Параметры:**
- `radius` (float): Радиус круга. Должен быть неотрицательным числом.

**Возвращает:**
- `float`: Площадь круга.

**Исключения:**
- `ValueError`: Если радиус отрицательный.
- `TypeError`: Если радиус не является числом.

### `triangle_area(side_a, side_b, side_c)`

Вычисляет площадь треугольника по трем сторонам, используя формулу Герона.

**Параметры:**
- `side_a` (float): Длина первой стороны треугольника.
- `side_b` (float): Длина второй стороны треугольника.
- `side_c` (float): Длина третьей стороны треугольника.

**Возвращает:**
- `float`: Площадь треугольника.

**Исключения:**
- `ValueError`: Если стороны не образуют валидный треугольник или являются неположительными.
- `TypeError`: Если стороны не являются числами.

## Примеры использования

```python
from geometry_calculator import circle_area, triangle_area

# Примеры для круга
print(circle_area(1))     # 3.141592653589793
print(circle_area(2.5))   # 19.634954084936208
print(circle_area(0))     # 0.0

# Примеры для треугольника
print(triangle_area(3, 4, 5))      # 6.0 (прямоугольный треугольник)
print(triangle_area(5, 5, 5))      # 10.825317547305483 (равносторонний)
print(triangle_area(5, 6, 7))      # 14.696938456699069

# Обработка ошибок
try:
    circle_area(-1)  # ValueError: Радиус должен быть неотрицательным числом
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    triangle_area(1, 2, 5)  # ValueError: Заданные стороны не образуют валидный треугольник
except ValueError as e:
    print(f"Ошибка: {e}")
```

## Тестирование

Запуск тестов с помощью unittest (встроенный модуль Python):

```bash
python -m unittest tests.test_shapes -v
```

Запуск всех тестов в директории tests:

```bash
python -m unittest discover tests -v
```

Запуск конкретного тестового класса:

```bash
python -m unittest tests.test_shapes.TestCircleArea -v
python -m unittest tests.test_shapes.TestTriangleArea -v
```

Альтернативно, можно использовать pytest (требует установки):

```bash
pip install pytest
python -m pytest tests/ -v
```

## Структура проекта

```
geometry_calculator/
├── geometry_calculator/
│   ├── __init__.py
│   └── shapes.py
├── tests/
│   ├── __init__.py
│   └── test_shapes.py
├── setup.py
├── requirements.txt
└── README.md
```

## Лицензия

None

## Автор

Shipilov Dmitriy, shipilenok1@gmail.com