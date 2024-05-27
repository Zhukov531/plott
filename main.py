from flask import Flask, blueprints

from routers.user import mod


app = Flask(__name__)


app.register_blueprint(mod)


app.run(debug=True)