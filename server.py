from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "Pinguinos"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    session['nombre'] = request.form['name']
    session['lugar'] = request.form['location']
    session['lenguage'] = request.form['language']
    session['comentario'] = request.form['comments']
    return redirect('/results')

@app.route("/results")
def show():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug = True)