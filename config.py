import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SuperSecretHavMun'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///sites.db'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'SecretJWT'
    JWT_TOKEN_LOCATION = ['headers']