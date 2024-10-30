from flask import Flask, request, jsonify, render_template, Blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import models

bp = Blueprint('main', __name__)

# Rutas
@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/edition')
def edition():
    return render_template('edition.html')

@bp.route('/our Team')
def our_team():
    return render_template('ourteam.html')

@bp.route('/history')
def history():
    return render_template('history.html')

@bp.route('/academic_design')
def academic_design():
    return render_template('academicdesign.html')

@bp.route('/take_part')
def take_part():
    return render_template('takepart.html')

@bp.route('/votation_system')
def votation_system():
    return render_template('login.html')

@bp.route('/contact_us')
def contact_us():
    return render_template('contact.html')

@bp.route('/resources')
def resources():
    return render_template('resources.html')

@bp.route('/comision1')
def comision1():
    return render_template('comision1.html')

@bp.route('/comision2')
def comision2():
    return render_template('comision2.html')

@bp.route('/comision3')
def comision3():
    return render_template('comision3.html')

@bp.route('/comision4')
def comision4():
    return render_template('comision4.html')

@bp.route('/comision5')
def comision5():
    return render_template('comision5.html')

@bp.route('/api/check_credentials', methods=["GET", "POST"])
def process_form():
    if request.method == "POST":
        
        country = request.form.get("country")
        comission = request.form.get("commission")
        password = request.form.get("password")

        print('Recivied Data:', country, comission, password)

        user = models.get_user_by_country(country)

        if not user:
            return jsonify({"msg": "El usuario no existe"}), 400
        if not user.check_password(password):
            return jsonify({"msg": "Contraseña incorrecta"}), 401
        
        access_token = create_access_token(identity=country)
        return render_template('acceptance.html', access_token=access_token)

    return render_template('loging.html')


@bp.route('/acceptance.html')
@jwt_required()
def acceptance():
    current_user = get_jwt_identity()
    return render_template('acceptance.html', current_user=current_user)
