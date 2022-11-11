from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Servidor en Ejecución"


#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

# Configurar variables de entorno
# export FLASK_APP=init
# export FLASK_ENV=development

# Iniciar proyecto
# flask run