from flask import Flask, render_template, request
from main import Solution

solve = Solution()
app = Flask(__name__)


def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    dic = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        dic[crs].append(pre)
    output = []
    visit, cycle = set(), set()

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True
        cycle.add(crs)
        for pre in dic[crs]:
            if dfs(pre) == False:
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True

    for c in range(numCourses):
        if dfs(c) == False:
            return []
    return output


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit-form', methods=['POST'])
def submit_form():
    text_input = request.form['text-input']
    second_text_input = request.form['second-text-input']
    if len(second_text_input) > 1:
        print(len(second_text_input))
        second_text_input = second_text_input.split(' ')
        print(second_text_input)
        iter_element = []
        for i in second_text_input:
            iter_element.append(i.split(','))

        for i in range(0, len(iter_element)):
            for j in range(0, 2):
                iter_element[i][j] = int(iter_element[i][j])
        print(iter_element)
    else:
        iter_element = []
    result = findOrder(numCourses=int(text_input), prerequisites=iter_element)
    return f'результат: {result}'


@app.errorhandler(Exception)
def handle_error(error):
    return render_template('error.html', error=error), 500


if __name__ == '__main__':
    app.run(debug=True)
