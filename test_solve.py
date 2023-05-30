import pytest

from main import Solution

solve = Solution()


@pytest.mark.parametrize("numCourses, prerequisites, expected_result", [(2, [[1, 0]], [0, 1]),
                                                                        (3, [[1, 0], [2, 1]], [0, 1, 2]),
                                                                        (3, [[2, 0], [1, 2]], [0, 2, 1])])
def test_positive_simple_data_work(numCourses, prerequisites, expected_result):
    """Проверка целой работоспособности алгоритма на простых данных"""
    assert solve.findOrder(numCourses=numCourses, prerequisites=prerequisites) == expected_result


def test_positive_min_num_courses():
    """Пололжительное минимальное пограничное значение переменной numCourses"""
    assert solve.findOrder(numCourses=1, prerequisites=[]) == [0]


def test_positive_max_num_courses():
    """Положительное максимальное пограничное значение переменной numCourses - 2000"""
    prerequisites = []
    expected_solve = []
    for i in range(1, 2000):
        prerequisites.append([i, i - 1])
        expected_solve.append(i - 1)
    expected_solve.append(1999)  # В силу различной нумерации курсов и экономии мозгов при чтении этого

    assert solve.findOrder(numCourses=2000, prerequisites=prerequisites) == expected_solve


def test_negative_max_num_courses():
    """Негативное максимальное пограничное значение перемнной numCourses - 2001"""
    prerequisites = []
    for i in range(1, 2001):
        prerequisites.append([i, i - 1])

    assert solve.findOrder(numCourses=2001, prerequisites=prerequisites) == "wrong numCourses"


def test_negative_min_num_courses():
    """Негативное минимальное пограничное значение переменной numCourses - 0"""
    assert solve.findOrder(numCourses=0, prerequisites=[]) == "wrong numCourses"


def test_negative_num_prerequisites():
    """Неверное кол-во аргументов prerequisites - 0 <= prerequisites.length <= numCourses * (numCourses - 1)"""
    assert solve.findOrder(numCourses=2, prerequisites=[[1, 0], [0, 1], [1, 0]]) == "wrong prerequisites"


def test_negative_format_prerequisites():
    """Неверно введеный формат prerequisites - prerequisites[i].length == 2"""
    assert solve.findOrder(numCourses=2, prerequisites=[[1, 0, 1]]) == "wrong prerequisites"