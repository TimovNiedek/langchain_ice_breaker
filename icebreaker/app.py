from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

from icebreaker.main import ice_break_with


load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    mock = request.form.get("mock", False)
    print(f"Processing {name} with mock={mock}")
    summary, profile_pic_url = ice_break_with(name, mock=mock)
    print(summary.dict())
    return jsonify({
        "summary_and_facts": summary.dict(),
        "picture_url": profile_pic_url
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

