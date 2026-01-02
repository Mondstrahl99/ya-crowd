"""Тесты для модуля calculator."""
import pytest
from src.calculator import Calculator

class TestCalculator:
    """Тестовый класс для Calculator."""
    
    @pytest.fixture
    def calc(self):
        """Фикстура для создания экземпляра калькулятора."""
        return Calculator()
    
    def test_add_positive_numbers(self, calc):
        """Тест сложения положительных чисел."""
        assert calc.add(2, 3) == 5
        assert calc.add(0, 0) == 0
        assert calc.add(-1, 1) == 0
    
    def test_subtract_numbers(self, calc):
        """Тест вычитания чисел."""
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(0, 5) == -5
        assert calc.subtract(10, 10) == 0
    
    def test_multiply_numbers(self, calc):
        """Тест умножения чисел."""
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(0, 5) == 0
        assert calc.multiply(-2, 3) == -6
    
    def test_divide_numbers(self, calc):
        """Тест деления чисел."""
        assert calc.divide(6, 2) == 3
        assert calc.divide(5, 2) == 2.5
        assert calc.divide(0, 5) == 0
    
    def test_divide_by_zero_raises_error(self, calc):
        """Тест деления на ноль вызывает исключение."""
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            calc.divide(5, 0)
    
    def test_power_operation(self, calc):
        """Тест возведения в степень."""
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1
        assert calc.power(4, 0.5) == 2
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),
        (0, 0, 0),
        (-1, -1, -2),
        (2.5, 2.5, 5),
    ])
    def test_add_with_params(self, calc, a, b, expected):
        """Параметризованный тест сложения."""
        assert calc.add(a, b) == expected
