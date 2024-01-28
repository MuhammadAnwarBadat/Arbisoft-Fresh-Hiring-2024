import requests
import datetime
import sys
import csv

def get_match_data(team1, team2):
    """Retrieves match data from the API for the given teams."""
    url = "https://l0l6pp2i0k.execute-api.eu-north-1.amazonaws.com/default/icc_matches"
    params = {"team1": team1, "team2": team2}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for error responses
    return response.json()

def calculate_weighted_score(team_score, match_date, current_year=2024):
    """Calculates the weighted score for a match based on its date."""
    try:
        years_ago = current_year - datetime.datetime.strptime(match_date, "%d/%m/%Y").year  # Adjusted format
    except ValueError:
        # Try the original format if the adjusted format fails
        try:
            years_ago = current_year - datetime.datetime.strptime(match_date, "%m/%d/%Y").year
        except ValueError:
            raise ValueError(f"Invalid date format: {match_date}")

    weight = max(0.5, 10 - years_ago)
    return team_score * weight

def predict_winner(team1, team2):
    """Predicts the winning chances for two teams based on historical data."""
    match_data = get_match_data(team1, team2)

    team1_wins = 0
    team2_wins = 0
    total_weight = 0

    for match in match_data:
        team1_score = sum(player["score"] for player in match["scoreCardTeam1"])
        team2_score = sum(player["score"] for player in match["scoreCardTeam2"])

        if team1_score > team2_score:
            team1_wins += calculate_weighted_score(team1_score, match["date"])
        elif team2_score > team1_score:
            team2_wins += calculate_weighted_score(team2_score, match["date"])

        total_weight += 10  # Assuming maximum 10 matches per year

    team1_percentage = (team1_wins / total_weight) * 100
    team2_percentage = (team2_wins / total_weight) * 100

    return f"{team1_percentage:.2f}%,{team2_percentage:.2f}%"

# Read input from file (using command-line argument)
if len(sys.argv) != 2:
    print("Usage: python championsTrophy.py input.txt")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r") as file:
    reader = csv.reader(input_file)
    teams = next(reader)  # Read the first (and only) row
    prediction = predict_winner(teams[0], teams[1])
    print(prediction)