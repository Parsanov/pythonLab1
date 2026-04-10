from flask import Flask, jsonify, render_template, request
from trips import trips

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route("/")
def MainPage():
    return render_template("index.html", trips=trips)

@app.route("/tour_operator")
def Findtour():
    value = request.args.get("findTour", default="")
    if value:
        result = [t for t in trips if t["туроператор"].lower() == value.lower()] 

    return render_template("operator.html", result=result)

@app.route("/tours")
def findDays():
    n = request.args.get("n", default=0, type=int)
    if n:
        result = [t for t in trips if t["кількість_днів"] >= n]
    return render_template("days.html", result=result)


@app.route("/the_most_expensive")
def Expensive():
    turkey = [t for t in trips if t["країна"] == "Туреччина"]
    if turkey:
        mostExp = max(turkey, key=lambda t: t["ціна"])
    return render_template("mostExp.html", mostExp=mostExp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)

