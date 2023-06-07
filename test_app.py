import pytest
from lib.apiwrapper import *


class TestClass:
    def test_get_from_http_status(self):
        assert get_form().status_code == 200

    def test_post_form_http_status(self):
        assert post_form(numCourses=3, prerequisites="1,0 2,1").status_code == 200

    def test_post_form_empty_http_status(self):
        assert post_form().status_code == 500

    def test_positive_simple_data_work(self):
        """Проверка целой работоспособности алгоритма на простых данных"""
        assert post_form(numCourses=3, prerequisites="1,0 2,1").text == '[0, 1, 2]'

    def test_positive_min_num_courses(self):
        """Пололжительное минимальное пограничное значение переменной numCourses"""
        assert post_form(numCourses=1, prerequisites="").text == '[0]'

    def test_positive_max_num_courses(self):
        """Положительное максимальное пограничное значение переменной numCourses - 2000"""
        prerequisites = ""
        expected_solve = []
        for i in range(1, 2000):
            prerequisites += str(i) + "," + str(i-1) + " "
            expected_solve.append(i - 1)
        expected_solve.append(1999)  # В силу различной нумерации курсов и экономии мозгов при чтении этого

        assert post_form(numCourses=2000, prerequisites=prerequisites).text == str(expected_solve)

    def test_negative_max_num_courses(self):
        """Негативное максимальное пограничное значение перемнной numCourses - 2001"""
        prerequisites = []
        for i in range(1, 2001):
            prerequisites.append([i, i - 1])

        assert post_form(numCourses=2001, prerequisites=prerequisites).status_code == 500

    def test_negative_min_num_courses(self):
        """Негативное минимальное пограничное значение переменной numCourses - 0"""
        assert post_form(numCourses=0, prerequisites=[]).status_code == 500

    def test_negative_num_prerequisites(self):
        """Неверное кол-во аргументов prerequisites - 0 <= prerequisites.length <= numCourses * (numCourses - 1)"""
        assert post_form(numCourses=2, prerequisites=[[1, 0], [0, 1], [1, 0]]).status_code == 500

    def test_negative_format_prerequisites(self):
        """Неверно введеный формат prerequisites - prerequisites[i].length == 2"""
        assert post_form(numCourses=2, prerequisites=[[1, 0, 1]]).status_code == 500
