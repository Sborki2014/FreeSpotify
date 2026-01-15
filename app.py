from flask import Flask, render_template, url_for
# render_template нужен для установления связи между html и flask
# url_for на всякий случай подключается, чтобы работал шаблонизатор.
app = Flask(__name__)


# Здесь мы обрабатываем страницу
@app.route('/')
@app.route('/home ')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/user/<string:name>/<int:id>')
def user (name, id):
    return 'User page: ' + name + ' - ' + str(id)
 
if __name__ == '__main__':
    app.run(debug=True) # True - Все различные ошибки будут выдавать на странице. False - Все ошибки будут выдаваться на сервере, чтобы пользователь их не видел 