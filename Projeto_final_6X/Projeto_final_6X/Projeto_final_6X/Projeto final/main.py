from flask import Flask
from flask import request
from flask import render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if name and email:
            registro = (name, email)

            try:
                conn = sqlite3.connect('cadastrar.db')

                sql = '''INSERT INTO cadastro(name, email)
                              VALUES(?,?)'''

                cur = conn.cursor()

                cur.execute(sql, registro)

                conn.commit()

                mensagem = 'Sucesso - cadastrado'
                return mensagem

            except:
                conn.rollback()
                mensagem = "erro em executar a operação"
            finally:
                return render_template("result.html", msg=mensagem)
                conn.close()

    return render_template('index.html')  # aqui temos a pagina incial


@app.route('/lista', methods=['GET', 'POST'])
def list():
    conn = sqlite3.connect("cadastrar.db")
    sql = "SELECT * FROM cadastro"
    cur = conn.cursor()
    cur.execute(sql)
    cadastros = cur.fetchall()
    return render_template('list.html', cad=cadastros)


@app.route('/sobre', methods=['GET', 'POST'])
def about():
    return render_template('sobre.html')


@app.route('/blog', methods=['GET', 'POST'])
def forum():
    return render_template('blog.html')


@app.route('/artigo1', methods=['GET', 'POST'])
def artigo1():
    return render_template('artigo1.html')

@app.route('/artigo2', methods=['GET', 'POST'])
def artigo2():
    return render_template('artigo2.html')

@app.route('/artigo3', methods=['GET', 'POST'])
def artigo3():
    return render_template('artigo3.html')

@app.route('/artigo4', methods=['GET', 'POST'])
def artigo4():
    return render_template('artigo4.html')

@app.route('/artigo5', methods=['GET', 'POST'])
def artigo5():
    return render_template('artigo5.html')

@app.route('/artigo6', methods=['GET', 'POST'])
def artigo6():
    return render_template('artigo6.html')


if __name__ == '__main__':
    app.run(debug=True)

