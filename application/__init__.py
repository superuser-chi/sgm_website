from flask import Flask
from application.sgm.views import sgm

app = Flask(__name__)
app.register_blueprint(sgm, url_prefix='/')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
