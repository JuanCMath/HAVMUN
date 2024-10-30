from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager
import os
import rsa

db = SQLAlchemy()
jwt = JWTManager()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(20), unique=True, nullable=False)
    comission = db.Column(db.Integer, nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def encrypt_password(password):
    private_key = os.environ['PRIVATE_KEY'].encode()
    encrypted_data = rsa.encrypt(password.encode(), public_key=private_key)
    return encrypted_data.hex()

def decrypt_password(encrypted_password):
    decrypted_data = bytes.fromhex(encrypted_password)
    decrypted_text = rsa.decrypt(decrypted_data, private_key=os.environ['PRIVATE_KEY'].encode()).decode()
    return decrypted_text

def create_user(country, password):
    user = User(country=country)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_country(country):
    return User.query.filter_by(country=country).first()