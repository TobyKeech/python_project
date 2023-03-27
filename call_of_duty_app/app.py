from flask import Flask, render_template
from controllers.cod_controller import codprofiles_blueprint
from controllers.weapon_controller import weapons_blueprint

app = Flask(__name__)

app.register_blueprint(codprofiles_blueprint)
app.register_blueprint(weapons_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)