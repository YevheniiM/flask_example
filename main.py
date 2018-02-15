from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def register():
    if "plus" in request.form:
        return render_template("success.html")
    if "minus" in request.form:
        return render_template("failure.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
