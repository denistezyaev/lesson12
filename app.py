from flask import Flask, request, render_template, send_from_directory
from main.main import main_bluprint
from loader.loader import loader_bluprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.register_blueprint(main_bluprint)
app.register_blueprint(loader_bluprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
