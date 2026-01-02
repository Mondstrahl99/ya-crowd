"""Модуль для математических операций."""
import logging

logger = logging.getLogger(__name__)

class Calculator:
    """Калькулятор для базовых математических операций."""
    
    def add(self, a: float, b: float) -> float:
        """Сложение двух чисел."""
        result = a + b
        logger.info(f"Сложение: {a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Вычитание двух чисел."""
        result = a - b
        logger.info(f"Вычитание: {a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Умножение двух чисел."""
        result = a * b
        logger.info(f"Умножение: {a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Деление двух чисел."""
        if b == 0:
            logger.error("Деление на ноль!")
            raise ValueError("Деление на ноль невозможно")
        result = a / b
        logger.info(f"Деление: {a} / {b} = {result}")
        return result
    
    def power(self, a: float, b: float) -> float:
        """Возведение в степень."""
        result = a ** b
        logger.info(f"Степень: {a} ^ {b} = {result}")
        return result
