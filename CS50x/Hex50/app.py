from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/binhex")
def binhex():
    return render_template("binhex.html")


@app.route("/bindec")
def bindec():
    return render_template("bindec.html")


@app.route("/binascii")
def binascii():
    return render_template("binascii.html")


@app.route("/binunicode")
def binunicode():
    return render_template("binunicode.html")

# hex
@app.route("/hexbin")
def hexbin():
    return render_template("hexbin.html")


@app.route("/hexdec")
def hexdec():
    return render_template("hexdec.html")


@app.route("/hexascii")
def hexascii():
    return render_template("hexascii.html")


@app.route("/hexuni")
def hexuni():
    return render_template("hexuni.html")

# unicode 

@app.route("/unidec")
def unidec():
    return render_template("unidec.html")


@app.route("/unibin")
def unibin():
    return render_template("unibin.html")


@app.route("/unihex")
def unihex():
    return render_template("unihex.html")

    # ascii


@app.route("/asciibin")
def asciibin():
    return render_template("asciibin.html")


@app.route("/asciidec")
def asciidec():
    return render_template("asciidec.html")


@app.route("/asciihex")
def asciihex():
    return render_template("asciihex.html")

# decimal

@app.route("/dechex")
def dechex():
    return render_template("dechex.html")


@app.route("/decbin")
def decbin():
    return render_template("decbin.html")

if __name__ == "__main__":
    app.run(debug=True)