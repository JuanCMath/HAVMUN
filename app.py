from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os, config, models
from cryptography.hazmat.primitives.asymmetric import rsa
from routes import bp


script_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(script_dir, 'templates')

if not os.path.exists(template_dir):
    print("Error: El directorio de templates no existe.")

def create_app():
    app = Flask(__name__, template_folder=template_dir)
    
    app.config.from_object(config.Config)
    app.register_blueprint(bp)
    models.db.init_app(app)
    models.jwt.init_app(app)

    with app.app_context():
        models.db.create_all()

    return app

# Generar claves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

# Guardar la clave privada encriptada
encrypted_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Guardar la clave pública
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Guardar las claves en archivos seguros
with open("private_key.pem", "wb") as f:
    f.write(encrypted_private_key)

with open("public_key.pem", "wb") as f:
    f.write(public_pem)


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        app.run(debug=True, port=4000)