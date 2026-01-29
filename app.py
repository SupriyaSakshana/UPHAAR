#region connection logic
from python_scripts import new_uphaar as uphaar
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from dotenv import load_dotenv
import os
import requests
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# MongoDB Atlas connection
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
base_uri = os.getenv("MONGODB_BASE_URI")

if not all([username, password, base_uri]):
    raise ValueError("Missing environment variables. Check your .env file.")

encoded_password = quote_plus(password)
uri = "mongodb+srv://apoorvakumar:"+encoded_password+"@cluster0.u6xrg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
print(f"Attempting to connect with URI: {uri}")  # Debug URI

try:
    # Increase server selection timeout to 10 seconds
    client = MongoClient(uri, serverSelectionTimeoutMS=10000)
    # Test connection immediately
    client.admin.command('ping')
    print("Connected to MongoDB Atlas successfully!")
except ServerSelectionTimeoutError as e:
    print(f"Server selection timeout error: {e}")
    raise
except Exception as e:
    print(f"Connection error: {e}")
    raise

db = client["uphaar"]
users_collection = db["users"]
#endregion
#region routing logic
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
# Explicitly enable template auto-reloading
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "Strong@123"

@app.route('/')
def index():
    return redirect(url_for('home'))

#region landing route
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

#region register route
import bcrypt
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if not all([name, email, password]):
            flash("All fields are required!")
            return redirect(url_for('register'))

        if users_collection.find_one({"email": email}):
            flash("Email already registered!")
            return redirect(url_for('register'))

        user_data = {"name": name, "email": email, "password": password}
        
        try:
            result = users_collection.insert_one(user_data)
            flash(f"Registration successful! User ID: {result.inserted_id}")
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"Error during registration: {e}")
            return redirect(url_for('register'))

    return render_template('register.html')
#endregion
#region login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not all([email, password]):
            flash("Email and password are required!")
            return redirect(url_for('login'))

        user = users_collection.find_one({"email": email})
        
        if user and user["password"] == password:  # Plain text for now
            flash(f"Login successful! Welcome, {user['name']}!")
            return redirect(url_for('gift'))  # Redirect to gift page
        else:
            flash("Invalid email or password!")
            return redirect(url_for('login'))

    return render_template('login.html')
#endregion

@app.route('/gift', methods = ['GET', 'POST'])
def gift():
    return render_template('gift.html')

features = ["suitable_for_profile", "preferences", "gift_description", "gift_category", "country"]
@app.route('/get_recommendation', methods = ['GET','POST'])
def get_recommendation():
    if request.method == 'POST' :
        gift_profile = request.form['gift_profile']
        gift_description = request.form['gift_description']
        gift_category = request.form['gift_category']
        your_country = request.form['your_country']
        # Create text string for prediction
        input_text = gift_profile+" "+gift_description+" "+gift_category+" "+your_country
        print("input text:"+input_text)

        # get the top 3 gift recommmendations
        gift_data = uphaar.recommend_gifts(input_text, 3)
        return gift_data
    return("done")

# @app.route("/show_recommendation")
# def show_recommendation(data):



@app.route('/logout')
def logout():
    flash("You have been logged out.")
    return redirect(url_for('login'))

# Load pretrained ML model (.pkl file)
model = None

if __name__ == '__main__':
    app.run(debug=True)
#endregion