from flask import Flask, render_template, url_for
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


if __name__ == '__main__':
    app.run(debug=True, port=4000)