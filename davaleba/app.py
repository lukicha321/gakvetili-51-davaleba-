from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hello')
def hello():
    title = "hello"
    content = "dzlean saintereso saiti"
    return render_template('hello.html', title=title, content=content)

if __name__ == '__main__':
    app.run(debug=True)