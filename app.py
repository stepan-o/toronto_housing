from flask import Flask
from flask import render_template

app = Flask(__name__)


def factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]


@app.route('/')
def main_page():
    return 'Greetings! You are on the main page!'


@app.route('/test/<var>')
def test_page(var):
    print(f'You are on the test page. Variable var = {var}.')
    return f'and capitalized, it would be {var.upper()}'


@app.route('/square/<int:num>')
def square_num(num):
    return str(num ** 2)


@app.route('/factors/<int:n>')
def factors_route(n):
    return render_template(
        "factors.html",
        num=n,
        factors=factors(n)
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
