from flask import Flask, jsonify, render_template, request
from trips import trips

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route("/")
def MainPage():
    return render_template("index.html", trips=trips)

@app.route("/tour_operator")
def Findtour():
    result = None
    value = request.args.get("findTour", default=None)
    if value:
        result = [t for t in trips if t["туроператор"].lower() == value.lower()]
    return render_template("operator.html", result=result, value=value)  # додай value=value

@app.route("/days")
def findDays():
    result = None
    n_raw = request.args.get("n")
    searched = "n" in request.args
    try:
        if n_raw is not None and n_raw != "":
            n = int(n_raw)
            result = [t for t in trips if t["кількість_днів"] >= n]
    except ValueError:
        result = []
    return render_template("days.html", result=result, searched=searched)

@app.route("/the_most_expensive")
def Expensive():
    mostExp = None
    turkey = [t for t in trips if t["країна"] == "Туреччина"]
    if turkey:
        mostExp = max(turkey, key=lambda t: t["ціна"])
    return render_template("mostExp.html", mostExp=mostExp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)

