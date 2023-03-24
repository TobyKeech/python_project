from flask import Flask, render_template
from controllers.cod_controller import codprofiles_blueprint

app = Flask(__name__)

app.register_blueprint(codprofiles_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)