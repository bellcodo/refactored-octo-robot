from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/activity_picker')
def show_entries():
    return render_template('show_entries.html', entries=entries)

if __name__ == "__main__":
    # go get the PORT from the environment
    port = os.environ.get("PORT")
    # run the app with the port and bind to any ip
    app.run(
      "0.0.0.0"
    , port
    )
