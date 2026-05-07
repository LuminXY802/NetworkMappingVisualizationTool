from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    """Brief description of index.

    Returns:
        Description of the return value.

    """
    return render_template('./frontend/index.html')


if __name__ == "__main__":
    app.run()