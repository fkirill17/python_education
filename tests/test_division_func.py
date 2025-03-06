from pytest_edu.utils import div
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (5, 2, 2.5),
                                                   (30, -3, -10), ])  # Декоратор позволяет передать несколько тестов
# в один тест
def test_div_good(a, b, expected_result):  # Тест
    assert div(a, b) == expected_result  # Тесткейс


@pytest.mark.parametrize("expected_exception, division, divider", [(ZeroDivisionError, 10, 0),
                                                                   (TypeError, 20, "2")])
def test_zero_division(expected_exception, divider, division):
    with pytest.raises(expected_exception):  # Проверяем выдаст ли функция ошибку, которую мы ожидаем
        div(division, divider)
