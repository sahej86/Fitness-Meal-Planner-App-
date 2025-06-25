from flask import Flask, render_template, request, redirect, url_for
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Define the data folder and file path
DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "meals.csv")

# Ensure the data/ directory exists
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)


def load_meals():
    meals = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["id"] = int(row["id"])
                row["calories"] = int(row["calories"])
                row["protein"] = int(row["protein"])
                row["carbs"] = int(row["carbs"])
                row["fat"] = int(row["fat"])
                meals.append(row)
    return meals


def save_meals(meals):
    with open(DATA_FILE, "w", newline='', encoding='utf-8') as f:
        fieldnames = [
            "id", "name", "category", "ingredients",
            "calories", "protein", "carbs", "fat",
            "instructions", "timestamp"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for meal in meals:
            writer.writerow(meal)


@app.route("/")
def index():
    meals = load_meals()
    return render_template("index.html", meals=meals)


@app.route("/add", methods=["GET", "POST"])
def add_meal():
    if request.method == "POST":
        meals = load_meals()
        new_id = max([meal["id"] for meal in meals], default=0) + 1
        new_meal = {
            "id": new_id,
            "name": request.form["name"],
            "category": request.form["category"],
            "ingredients": request.form["ingredients"],
            "calories": int(request.form.get("calories", 0)),
            "protein": int(request.form.get("protein", 0)),
            "carbs": int(request.form.get("carbs", 0)),
            "fat": int(request.form.get("fat", 0)),
            "instructions": request.form.get("instructions", ""),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        meals.append(new_meal)
        save_meals(meals)
        return redirect(url_for("index"))
    return render_template("add_meal.html")


@app.route("/view/<int:meal_id>")
def view_meal(meal_id):
    meals = load_meals()
    meal = next((m for m in meals if m["id"] == meal_id), None)
    if meal:
        return render_template("view_meal.html", meal=meal)
    return redirect(url_for("index"))


@app.route("/edit/<int:meal_id>", methods=["GET", "POST"])
def edit_meal(meal_id):
    meals = load_meals()
    meal = next((m for m in meals if m["id"] == meal_id), None)
    if not meal:
        return redirect(url_for("index"))

    if request.method == "POST":
        meal["name"] = request.form["name"]
        meal["category"] = request.form["category"]
        meal["ingredients"] = request.form["ingredients"]
        meal["calories"] = int(request.form.get("calories", 0))
        meal["protein"] = int(request.form.get("protein", 0))
        meal["carbs"] = int(request.form.get("carbs", 0))
        meal["fat"] = int(request.form.get("fat", 0))
        meal["instructions"] = request.form.get("instructions", "")
        save_meals(meals)
        return redirect(url_for("view_meal", meal_id=meal_id))

    return render_template("edit.html", meal=meal)


@app.route("/delete/<int:meal_id>", methods=["POST"])
def delete_meal(meal_id):
    meals = load_meals()
    meals = [m for m in meals if m["id"] != meal_id]
    save_meals(meals)
    return redirect(url_for("index"))


@app.route("/plan", methods=["GET", "POST"])
def meal_plan():
    meals = load_meals()
    selected_meals = []
    totals = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}

    if request.method == "POST":
        ids = request.form.getlist("meal_ids")
        selected_meals = [m for m in meals if str(m["id"]) in ids]
        for m in selected_meals:
            totals["calories"] += m["calories"]
            totals["protein"] += m["protein"]
            totals["carbs"] += m["carbs"]
            totals["fat"] += m["fat"]

    return render_template("meal_plan.html", meals=meals, selected_meals=selected_meals, totals=totals)


if __name__ == "__main__":
    app.run(debug=True)
