from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from models import db
from ai_routes import ai_bp

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hydrogengolf.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(ai_bp)

@app.route("/")
def index():
    return render_template("index.html", project_name="Hydrogen Golf")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
