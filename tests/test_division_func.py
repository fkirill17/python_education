from pytest_edu.division_func import div
import pytest


def test():  # Тест
    assert div(1, 2) == 0.5  # Тесткейс


def test_2():
    with pytest.raises(ZeroDivisionError):  # Проверяем что функция вернет именно эту ошибку
        div(1, 0)


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (5, 2, 2.5),
                                                   (30, -3, -10), ])  # Декоратор для запуска одного теста
# с разными входными параметрами
def test_div_good(a, b, expected_result):
    assert div(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, division, divider", [(ZeroDivisionError, 10, 0),
                                                                   (TypeError, 20, "2")])
def test_zero_division(expected_exception, divider, division):
    with pytest.raises(expected_exception):  # Проверяем выдаст ли функция ошибку, которую мы ожидаем
        div(division, divider)
