from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/home2')
def home2():
    return render_template('index2.html')


# @app.route('/innastrona', methods=['GET'])
# def innastrona():
#     return 'Witam na innej stronie'
# @app.route('/klient/<numer>')
# def klient(numer):
#     return f'Klient o numerze {numer} to ...'
# @app.route('/dodaj/<numer1>+<numer2>')
# def dodaj(numer1,numer2):
#     wynik = int(numer1) + int(numer2)
#     return f'Wynik: {wynik}'

if __name__ == '__main__':
    app.run(debug=True)