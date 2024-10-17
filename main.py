from flask import Flask, render_template, request
from TrajectoryPlotter import *
import os

IMAGE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if os.path.exists("static/images/output.png"):
        os.remove("static/images/output.png")
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        mode = request.form.get('mode')
        name = request.form.get('description')
        print(f"The name is: {name}")
        print(f"The mode is: {mode}")
        try:
            plot_trajectory(f.filename)
        except Exception as e:
            return render_template("Error.html")
            
        full_filename = os.path.join(app.config['IMAGE_FOLDER'], 'output.png')
        return render_template("Acknowledgement.html", name=f.filename, plot_path=full_filename)


if __name__ == "__main__":
    app.run(debug=True)
