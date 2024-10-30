from flask import Flask, jsonify, request, render_template 
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os
import models

script_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(script_dir, 'templates')

if not os.path.exists(template_dir):
    print("Error: El directorio de templates no existe.")
else:
    print("Contenido del directorio de templates:")
    for item in os.listdir(template_dir):
        print(item)

app = Flask(__name__, template_folder=template_dir)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['SECRET_KEY'] = 'SuperSecretHavMun'
app.config["JWT_SECRET_KEY"] = 'SecretJWT'
app.config['JWT_TOKEN_LOCATION'] = ['headers']


db = SQLAlchemy(app)
#JWT Initialization
jwt = JWTManager(app)

with app.app_context():
    db.create_all()
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

@app.route('/comision1')
def comision1():
    return render_template('comision1.html')

@app.route('/comision2')
def comision2():
    return render_template('comision2.html')

@app.route('/comision3')
def comision3():
    return render_template('comision3.html')

@app.route('/comision4')
def comision4():
    return render_template('comision4.html')

@app.route('/comision5')
def comision5():
    return render_template('comision5.html')

@app.route('/api/check_credentials', methods=["GET", "POST"])
def process_form():
    if request.method == "POST":
        
        country = request.form.get("country")
        comision = request.form.get("commission")
        password = request.form.get("password")

        print('Recivied Data:', country, comision, password)


        if not country or not comision or not password:
            return render_template('login.html', message = "Please fill all fields")
        
        user = User.query.filter_by(country= country).first()

        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(indentity= user.id)
            print('Login Success access_token:', access_token)
            return get_country
        else:
            return jsonify({'message': 'Login Failed'}), 401

    return render_template('resources.html')


@app.route('/get_country', methods = ['GET'])
@jwt_required()
def get_country():
    user_id = get_jwt_identity()
    print(user_id)
    user = User.query.filter_by(id=user_id).first()

    if user:
        return jsonify({'message': 'User found', 'country': user.country})
    else:
        return jsonify({'message': 'User not found'}), 404



if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, port=4000)