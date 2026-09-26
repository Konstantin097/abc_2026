# todo: добавьте во Flask маршруты для страниц (endpoint)
#- О компании
#- Контакты
#- Список постов

from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_page():
    return "Это основная страница"


@app.route("/about")
def about_the_company():
    return "Это страница с информацией о компании"


@app.route("/contacts")
def contacts():
    return "Это страница с контактами"


@app.route("/posts")
def posts():
    return "Это страница со списком постов"

if __name__ == "__main__":
    app.run()
