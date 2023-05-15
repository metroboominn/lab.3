from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        num_1 = float(request.form.get('num_1'))
        num_2 = float(request.form.get('num_2'))
        num_3 = float(request.form.get('num_3'))
        d = num_2**2-4*num_1*num_3
        if d > 0:
            x1 = (num_2*(-1) + d ** 0.5) / (2 * num_1)
            x2 = (num_2*(-1) - d ** 0.5) / (2 * num_1)
            ans = "При a = " + str(num_1) + ", b = " + str(num_2) + ", с = " + str(num_3) + ", уравнение имеет два действительных корня: x1 = " + str(x1) + ", x2 = " + str(x2)
        elif d == 0:
            x1 = (num_2 * (-1) + d ** 0.5) / (2 * num_1)
            ans = "При a = " + str(num_1) + ", b = " + str(num_2) + ", с = " + str(num_3) + ", уравнение имеет один действительный корень: x = " + str(x1)
        else:
            ans = "При a = " + str(num_1) + ", b = " + str(num_2) + ", с = " + str(num_3) + ", уравнение не имеет действительных корней."
        return render_template('index.html', ans=ans)


if __name__ == '__main__':
    app.run()