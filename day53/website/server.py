from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Assuming you have a hello.html template

if __name__ == "__main__":
    app.run(debug=True)
