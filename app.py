from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html', title='home')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)