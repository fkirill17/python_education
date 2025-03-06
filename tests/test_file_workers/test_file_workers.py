from pytest_edu.file_workers import read_from_file


def create_test_data(test_data):
    with open("tests/test_file_workers/testfile.txt", "a") as file_object:
        file_object.writelines(test_data)


def test_readr_from_file():
    test_data = ['one\n', 'two\n', 'three']
    create_test_data(test_data)
    assert test_data == read_from_file("tests/test_file_workers/testfile.txt")


def test_read_fom_file_2():
    test_data = ['one\n', 'two\n', 'three']
    create_test_data(test_data)
    assert test_data == read_from_file("tests/test_file_workers/testfile.txt")
