# Meal Tracker - Health Nutrition & Planner App

A simple yet expandable web application to help users manage meals, calculate nutrition, and plan healthy eating habits. Built using Flask and currently stores data in a CSV file (`meals.csv`) for ease of access and portability.

---

## 👨‍💻 Project Team

- **Project Lead:** Sahej Kadam  
- **UI/UX Design:** Purvank Lakhani  
- **Backend Developers:** Sahej Kadam, Purvank Lakhani  

---

## 🚀 Features

✅ Add, view, edit, and delete meal entries  
✅ Store meal data in a CSV file (`meals.csv`)  
✅ Filter meals by category or search by name  
✅ Calculate total calories, protein, carbs, and fat for selected meals  
✅ Responsive and intuitive UI using HTML/CSS + Jinja templating  
✅ Flash alerts for instant feedback (e.g., missing fields, successful updates)  

---

## 🔮 Planned Future Features

🧠 Auto-calculation of nutrients via external API (based on food + quantity)  
🔐 User authentication and login system  
🧾 Switch from CSV to a real-time database (SQLite/PostgreSQL)  
📱 Smartwatch integration for sleep tracking, steps, oxygen levels  
🧠 Autocomplete search for food names  

---

## 🧱 Technologies Used

- Python (Flask)  
- HTML5, CSS3, Bootstrap  
- CSV (data handling using Python's `csv` module)  
- Jinja2 templating  
- JavaScript (for interactivity)  
- [Planned] Nutrition API, SQLite/PostgreSQL, Watch SDKs  

---

## 📸 UI Preview

**1. Meal Dashboard – View All Meals**  
A clean table interface displaying all meals with nutritional info and action buttons.  
_(Screenshot: index.html)_

**2. Add Meal Form**  
Intuitive form flow with fields for nutritional values, ingredients, and instructions.  
_(Screenshot: add_meal.html)_

**3. Meal Planner**  
Select meals and calculate total nutrition in one click.  
_(Screenshot: meal_plan.html)_

**4. Project Structure in VS Code**  
Neatly organized folders with clear separation of templates, static assets, and data files.  
_(Screenshot: folder view)_

---

## ⚙️ Setup Instructions


1. Clone or extract the project folder
   Download or clone the repository using Git or a ZIP archive.

2. (Recommended) Create a virtual environment
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies
   pip install flask

4. Run the Flask app
   python app.py

5. Launch your browser and open:
   http://127.0.0.1:5000/