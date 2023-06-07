import requests
BASE_URL = 'http://localhost:5000/'


def get_form():
    response = requests.get(BASE_URL)
    return response


def post_form(numCourses=None, prerequisites=None):
    post_data = {'numCourses': numCourses, 'prerequisites': prerequisites}
    response = requests.post(BASE_URL, data=post_data)
    return response

