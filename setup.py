"""
Скрипт установки для geometry_calculator.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geometry_calculator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Библиотека для вычисления площадей геометрических фигур",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/geometry_calculator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Библиотека использует только стандартную библиотеку Python
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",  # Опционально, для альтернативы unittest
            "pytest-cov>=2.0",  # Для покрытия кода
        ],
    },
    include_package_data=True,
    zip_safe=False,
) 