"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)
        assert 292 == calculator.add(124, 168)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)
        assert -20 == calculator.subtract(3, 23)

    def test_multiply(self):
        assert 4 == calculator.multiply(2, 2)
        assert 22 == calculator.multiply(2, 11)

    def test_divide(self):
        assert 5.0 == calculator.divide(10, 2)
        assert 5.5 == calculator.divide(11, 2)
