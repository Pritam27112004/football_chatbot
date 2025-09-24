from flask import Flask, render_template, request
from scraper import get_club_schedule



# Example club mapping: id and url name for ESPN
CLUBS = {
    "Liverpool": {"id": 364, "name": "liverpool"},
    "Manchester United": {"id": 360, "name": "manchester-united"},
    "Arsenal": {"id": 359, "name": "arsenal"},
    "Chelsea": {"id": 363, "name": "chelsea"},
    # Add more clubs as needed
}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    clubs = list(CLUBS.keys())
    if request.method == "POST":
        club = request.form["club"]
        club_info = CLUBS.get(club)
        if club_info:
            fixtures = get_club_schedule(club_info["id"], club_info["name"])
            return render_template("club_matches.html", club=club, fixtures=fixtures, clubs=clubs)
        else:
            message = f"Club '{club}' not found. Please select a valid club."
            return render_template("index.html", message=message, clubs=clubs)
    return render_template("index.html", message=message, clubs=clubs)

if __name__ == "__main__":
    app.run(debug=True)
