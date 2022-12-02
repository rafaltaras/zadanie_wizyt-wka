from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template('index1.html')

@app.route('/mypage/contact', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template('index2.html')
    if request.method == 'POST':
        message = request.form['message']
        return render_template('message.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)