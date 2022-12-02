from flask import Flask
from flask import request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return 'Witam na  stronie'



if __name__ == '__main__':
    app.run(debug=True)