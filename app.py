from flask import Flask, jsonify, session, request, redirect, url_for, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
import sqlite3 
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(script_dir, 'templates')

if not os.path.exists(template_dir):
    print("Error: El directorio de templates no existe.")
else:
    print("Contenido del directorio de templates:")
    for item in os.listdir(template_dir):
        print(item)

app = Flask(__name__, template_folder=template_dir)

# Rutas
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/edition')
def edition():
    return render_template('edition.html')

@app.route('/our Team')
def our_team():
    return render_template('ourteam.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/academic_design')
def academic_design():
    return render_template('academicdesign.html')

@app.route('/take_part')
def take_part():
    return render_template('takepart.html')

@app.route('/votation_system')
def votation_system():
    return render_template('login.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')


@app.route('/api/check_credentials', methods=["GET", "POST"])
def process_form():
    if request.method == "POST":
        
        country = request.form.get("country")
        comision = request.form.get("commission")
        psw = request.form.get("password")

        if not country or not comision or not psw:
            return render_template('login.html', message = "Please fill all fields")
        
        print(f"submitted: {country} {comision} {psw}")

        #cambiar aqui despues de acceptar con JWT el usuario a que pagina se tiene que dirigir
        return render_template('acceptance.html')

    return render_template('resources.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)