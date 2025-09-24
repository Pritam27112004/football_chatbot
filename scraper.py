import requests
from bs4 import BeautifulSoup

def get_club_schedule(club_id, club_name):
    url = f"https://www.espn.com/soccer/team/fixtures/_/id/{club_id}/{club_name.lower()}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    fixtures = []
    rows = soup.select("table tbody tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 3:
            # ESPN usually formats as: date, opponent, comp, time (sometimes)
            date_time = cols[0].get_text(strip=True)
            opponent = cols[1].get_text(strip=True)
            comp = cols[2].get_text(strip=True)
            # Try to extract time if present (sometimes in a 4th column)
            time = cols[3].get_text(strip=True) if len(cols) > 3 else "TBD"
            fixtures.append({
                "club1": club_name.title(),
                "club2": opponent,
                "date_time": date_time,
                "time": time,
                "competition": comp
            })

    return fixtures if fixtures else []
