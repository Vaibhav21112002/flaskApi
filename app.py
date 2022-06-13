from flask import Flask
import db
from controllers.users import user

app = Flask(__name__)


@app.route('/', methods=['GET'])
def check():
    return "All OK"


app.register_blueprint(user, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
