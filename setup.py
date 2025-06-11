"""
Скрипт установки для geometry_calculator.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geometry_calculator",
    version="2.0.0",
    author="Shipilov Dmitriy",
    author_email="shipilenok1@gmail.com",
    description="Современная библиотека для вычисления площадей геометрических фигур с поддержкой полиморфизма",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/geometry_calculator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "Typing :: Typed",
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