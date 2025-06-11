# Geometry Calculator v2.0

Современная библиотека для вычисления площадей геометрических фигур с поддержкой полиморфизма и легкой расширяемости.

## ✨ Основные возможности

- **🔺 Вычисление площади треугольника** по трем сторонам (формула Герона)
- **⭕ Вычисление площади круга** по радиусу
- **🔍 Проверка прямоугольного треугольника** (теорема Пифагора)
- **🔄 Полиморфное вычисление площади** без знания типа фигуры в compile-time
- **➕ Легкость добавления новых фигур** через наследование
- **✅ Валидация входных данных** и обработка ошибок
- **🔄 Обратная совместимость** с предыдущими версиями

## 📦 Установка

```bash
pip install geometry_calculator
```

Для разработки:
```bash
git clone <repository-url>
cd geometry_calculator
pip install -e .
pip install -r requirements-dev.txt  # Dev зависимости
```

## 🚀 Быстрый старт

### Новый API (рекомендуется)

```python
from geometry_calculator import Circle, Triangle, calculate_area, is_right_triangle

# Создание фигур
circle = Circle(5)
triangle = Triangle(3, 4, 5)

# Вычисление площади
print(f"Площадь круга: {circle.area()}")           # 78.54
print(f"Площадь треугольника: {triangle.area()}")  # 6.0

# Полиморфное вычисление площади
shapes = [circle, triangle]
for shape in shapes:
    area = calculate_area(shape)  # Работает с любой фигурой!
    print(f"{shape} → Площадь: {area}")

# Проверка прямоугольного треугольника
print(f"Прямоугольный: {triangle.is_right_triangle()}")  # True
print(f"Прямоугольный: {is_right_triangle(3, 4, 5)}")   # True
```

### Legacy API (для обратной совместимости)

```python
from geometry_calculator import circle_area, triangle_area

# Старый способ (по-прежнему работает)
area1 = circle_area(5)
area2 = triangle_area(3, 4, 5)
```

## 📖 Подробная документация

### Классы фигур

#### `Circle(radius)`

Класс для представления круга.

**Параметры:**
- `radius` (float): Радиус круга. Должен быть неотрицательным числом.

**Методы:**
- `area()` → float: Вычисляет площадь круга (π × r²)

**Пример:**
```python
circle = Circle(5)
print(circle.area())  # 78.53981633974483
print(str(circle))    # Круг(радиус=5)
```

#### `Triangle(side_a, side_b, side_c)`

Класс для представления треугольника.

**Параметры:**
- `side_a, side_b, side_c` (float): Длины сторон треугольника.

**Методы:**
- `area()` → float: Вычисляет площадь треугольника (формула Герона)
- `is_right_triangle()` → bool: Проверяет, является ли треугольник прямоугольным

**Пример:**
```python
triangle = Triangle(3, 4, 5)
print(triangle.area())              # 6.0
print(triangle.is_right_triangle()) # True
print(str(triangle))                # Треугольник(стороны=3, 4, 5)
```

### Полиморфные функции

#### `calculate_area(shape: Shape)`

Вычисляет площадь любой геометрической фигуры без знания её типа в compile-time.

**Параметры:**
- `shape` (Shape): Экземпляр любого класса, наследующего от Shape.

**Возвращает:**
- `float`: Площадь фигуры.

**Пример:**
```python
shapes = [Circle(3), Triangle(3, 4, 5)]
for shape in shapes:
    print(f"Площадь {shape}: {calculate_area(shape)}")
```

#### `is_right_triangle(side_a, side_b, side_c)`

Проверяет, является ли треугольник с заданными сторонами прямоугольным.

**Параметры:**
- `side_a, side_b, side_c` (float): Длины сторон треугольника.

**Возвращает:**
- `bool`: True, если треугольник прямоугольный.

**Пример:**
```python
print(is_right_triangle(3, 4, 5))  # True
print(is_right_triangle(2, 3, 4))  # False
```

## 🔧 Расширение библиотеки

Добавление новых фигур очень простое:

```python
from geometry_calculator import Shape, calculate_area

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Прямоугольник({self.width}x{self.height})"

# Автоматически работает с полиморфными функциями!
rect = Rectangle(4, 6)
area = calculate_area(rect)  # 24.0
```

Больше примеров в файле `examples/extensibility_demo.py`.

## 🧪 Тестирование

Запуск тестов с помощью unittest:

```bash
# Все тесты
python -m unittest discover tests -v

# Конкретный файл
python -m unittest tests.test_shapes -v

# Конкретный класс тестов
python -m unittest tests.test_shapes.TestCircleClass -v
python -m unittest tests.test_shapes.TestTriangleClass -v
python -m unittest tests.test_shapes.TestPolymorphicFunctions -v
```

Альтернативно с pytest:

```bash
pip install pytest
python -m pytest tests/ -v
```

## 📁 Структура проекта

```
geometry_calculator/
├── geometry_calculator/           # Основной пакет
│   ├── __init__.py               # Экспорты и метаданные
│   └── shapes.py                 # Классы фигур и функции
├── tests/                        # Тесты
│   ├── __init__.py              
│   └── test_shapes.py           # Полный набор тестов
├── examples/                     # Примеры использования
│   └── extensibility_demo.py    # Демонстрация расширяемости
├── setup.py                     # Конфигурация пакета
├── requirements.txt             # Зависимости
├── example.py                   # Основные примеры
├── MANIFEST.in                  # Манифест пакета
└── README.md                    # Документация
```

## 🎯 Ключевые преимущества v2.0

### ✅ Все требования выполнены:

1. **Легкость добавления других фигур**
   - Простое наследование от базового класса `Shape`
   - Автоматическая поддержка полиморфизма

2. **Вычисление площади без знания типа в compile-time**
   - Функция `calculate_area()` работает с любыми фигурами
   - Полный полиморфизм через абстрактные методы

3. **Проверка прямоугольного треугольника**
   - Метод `Triangle.is_right_triangle()`
   - Функция `is_right_triangle(a, b, c)`
   - Высокая точность вычислений (погрешность < 1e-10)

### 🏗️ Архитектурные улучшения:

- **SOLID принципы**: Каждый класс имеет одну ответственность
- **Открытость/Закрытость**: Легко расширять, не изменяя существующий код  
- **Полиморфизм**: Единообразный интерфейс для всех фигур
- **Обратная совместимость**: Старый API продолжает работать

## 📋 Примеры использования

```python
from geometry_calculator import *

# Различные способы создания и использования
circle = Circle(5)
triangle = Triangle(3, 4, 5)

# Способ 1: Методы объектов
print(f"Площадь круга: {circle.area()}")
print(f"Треугольник прямоугольный: {triangle.is_right_triangle()}")

# Способ 2: Полиморфные функции
shapes = [circle, triangle]
total_area = sum(calculate_area(shape) for shape in shapes)
print(f"Общая площадь: {total_area}")

# Способ 3: Legacy функции
area1 = circle_area(5)          # Deprecated, но работает
area2 = triangle_area(3, 4, 5)  # Deprecated, но работает

# Способ 4: Проверка прямоугольности
is_right = is_right_triangle(3, 4, 5)  # True

# Обработка ошибок
try:
    invalid_triangle = Triangle(1, 2, 5)  # ValueError
except ValueError as e:
    print(f"Ошибка: {e}")
```

## 🚀 Миграция с v1.x

Если вы использовали v1.x, ваш код продолжит работать без изменений:

```python
# v1.x код - работает в v2.0
from geometry_calculator import circle_area, triangle_area
area1 = circle_area(5)
area2 = triangle_area(3, 4, 5)
```

Рекомендуется постепенно переходить на новый API:

```python
# Новый рекомендуемый подход в v2.0
from geometry_calculator import Circle, Triangle, calculate_area
circle = Circle(5)
triangle = Triangle(3, 4, 5)
area1 = calculate_area(circle)
area2 = calculate_area(triangle)
```

## 📄 Лицензия

None

## 👨‍💻 Автор

**Shipilov Dmitriy**  
📧 shipilenok1@gmail.com

---

**Версия:** 2.0.0  
**Python:** ≥ 3.7  
**Зависимости:** Только стандартная библиотека Python