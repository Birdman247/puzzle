from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_crossword_clue(clue_number, direction):
    url = "https://birdman247.github.io/puzzle/"

    response = requests.get(url)
    if response.status_code == 200:
    
        soup = BeautifulSoup(response.content, "html.parser")

        clue_element = soup.find("div", {"data-cellnum": clue_number, "data-dir": direction})

        if clue_element:
            clue_text = clue_element.text.strip()
            return clue_text
        else:
            return "Clue not found"
    else:
        return "Failed to retrieve the crossword puzzle"

@app.route("/", methods=["GET", "POST"])
def crossword_interface():
    if request.method == "POST":
        clue_number = request.form.get("clue_number")
        direction = request.form.get("direction")

        clue = get_crossword_clue(clue_number, direction)

        return render_template("index.html", clue=clue)

    return render_template("index.html", clue="")

if __name__ == "__main__":
    app.run(debug=True)

