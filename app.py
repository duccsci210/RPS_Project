from flask import Flask, request, jsonify
import random

# Initialize the Flask application
app = Flask(__name__)

# Central Data Store (Leaderboard)
LEADERBOARD = {}

# Default route
@app.route('/')
def home():
    return "Welcome to Rock-Paper-Scissors!"

# Player Registration Route
@app.route('/api/player/register', methods=['POST'])
def register_player():
    data = request.get_json()
    player_name = data.get('name')

    if player_name in LEADERBOARD:
        return jsonify({"message": f"Player {player_name} already exists."}), 400
    
    LEADERBOARD[player_name] = {"score": 0, "games_won": 0}
    return jsonify({"message": f"Player {player_name} registered successfully."}), 201

# Game Start Route
@app.route('/api/game/start', methods=['POST'])
def start_game():
    data = request.get_json()
    player1 = data.get('player1')
    player2 = data.get('player2')

    if player1 not in LEADERBOARD or player2 not in LEADERBOARD:
        return jsonify({"message": "Both players must be registered."}), 400

    LEADERBOARD[player1]['score'] = 0
    LEADERBOARD[player2]['score'] = 0
    return jsonify({"message": f"Game started successfully between {player1} and {player2}."}), 200

# Play Round Route
@app.route('/api/game/play_round', methods=['POST'])
def play_round():
    data = request.get_json()
    player1 = data.get('player1')
    player2 = data.get('player2')
    player1_choice = data.get('player1_choice')
    player2_choice = data.get('player2_choice')

    if player1 not in LEADERBOARD or player2 not in LEADERBOARD:
        return jsonify({"message": "Both players must be registered."}), 400
    
    # Check if player scores are None and initialize them if necessary
    if LEADERBOARD[player1].get('score') is None:
        LEADERBOARD[player1]['score'] = 0
    if LEADERBOARD[player2].get('score') is None:
        LEADERBOARD[player2]['score'] = 0

    valid_choices = ['rock', 'paper', 'scissors']
    if player1_choice not in valid_choices or player2_choice not in valid_choices:
        return jsonify({"message": "Invalid choice! Choose from 'rock', 'paper', or 'scissors'."}), 400

    # Determine the winner of the round
    if player1_choice == player2_choice:
        result = "It's a tie!"
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
         (player1_choice == 'scissors' and player2_choice == 'paper') or \
         (player1_choice == 'paper' and player2_choice == 'rock'):
        result = f"{player1} wins!"
        LEADERBOARD[player1]['score'] += 1
        LEADERBOARD[player1]['games_won'] += 1
    else:
        result = f"{player2} wins!"
        LEADERBOARD[player2]['score'] += 1
        LEADERBOARD[player2]['games_won'] += 1

    return jsonify({"message": result, "leaderboard": LEADERBOARD}), 200

# Leaderboard Route
@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    sorted_by_name = sorted(LEADERBOARD.items(), key=lambda x: x[0])
    sorted_by_score = sorted(LEADERBOARD.items(), key=lambda x: x[1]['score'], reverse=True)
    
    leaderboard = {
        "sorted_by_name": sorted_by_name,
        "sorted_by_score": sorted_by_score
    }

    return jsonify(leaderboard), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
