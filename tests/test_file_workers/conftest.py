import pytest


@pytest.fixture(autouse=True)  # Функция обернутая в декоратор fixture будет срабатывать при каждом тесте
def clean_test_file():
    with open("tests/test_file_workers/testfile.txt", "w"):  # Очистка текстового файла
        pass
