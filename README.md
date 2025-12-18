
# Rock-Paper-Scissors Tournament (Flask)

This is a Flask API for a simple Rock-Paper-Scissors game with a leaderboard powered by a dictionary.

## 1. Setup Instructions

### Step 1: Clone the Repository
Ensure you have the project files saved in a directory.

### Step 2: Set up the Virtual Environment
Open PowerShell or Command Prompt and navigate to the project directory where your `app.py` is located:
```
cd C:\Users\ngomi\RPS_Project
```

Create a virtual environment:
```
py -m venv myenv
```

Activate the virtual environment:
```
.\myenv\Scripts\Activate
```

### Step 3: Install Dependencies
Ensure you have all necessary dependencies installed:
```
pip install -r requirements.txt
```

### Step 4: Run the Application
Finally, run the Flask application with the following command:
```
py app.py
```

This will start the server at `http://127.0.0.1:5000`.

## 2. API Endpoints

### 2.1 Register a New Player
- **Endpoint:** `/api/player/register`
- **Method:** `POST`
- **Description:** Registers a new player.
- **Request Body:**
    ```json
    {
        "name": "Player1"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Player Player1 registered successfully."
    }
    ```
- **Status Code:** `201 CREATED`

### 2.2 Start a New Game
- **Endpoint:** `/api/game/start`
- **Method:** `POST`
- **Description:** Starts a new game between two players.
- **Request Body:**
    ```json
    {
        "player1": "Player1",
        "player2": "Player2"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Game started successfully between Player1 and Player2."
    }
    ```
- **Status Code:** `200 OK`

### 2.3 Play a Round
- **Endpoint:** `/api/game/play_round`
- **Method:** `POST`
- **Description:** Executes one round of Rock-Paper-Scissors between two players.
- **Request Body:**
    ```json
    {
        "player1": "Player1",
        "player2": "Player2",
        "player1_choice": "rock",
        "player2_choice": "scissors"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Player1 wins!",
        "leaderboard": {
            "Player1": {
                "games_won": 1,
                "score": 1
            },
            "Player2": {
                "games_won": 0,
                "score": 0
            }
        }
    }
    ```
- **Status Code:** `200 OK`

### 2.4 Get Leaderboard
- **Endpoint:** `/api/leaderboard`
- **Method:** `GET`
- **Description:** Retrieves the current leaderboard, sorted by player name and score.
- **Response:**
    ```json
    {
        "sorted_by_name": [
            ["Player1", {"games_won": 1, "score": 1}],
            ["Player2", {"games_won": 0, "score": 0}]
        ],
        "sorted_by_score": [
            ["Player1", {"games_won": 1, "score": 1}],
            ["Player2", {"games_won": 0, "score": 0}]
        ]
    }
    ```
- **Status Code:** `200 OK`

## 3. How to Test the API Using Postman

### Step 1: Set up Postman
1. Open Postman and make sure your Flask server is running (`py app.py`).
2. Use Postman to interact with the API.

### Step 2: Register a New Player
1. Select `POST` in the request type dropdown.
2. Enter the URL: `http://127.0.0.1:5000/api/player/register`.
3. Go to the **Body** tab, select **raw**, and choose **JSON** format.
4. Enter the player’s name:
    ```json
    {
        "name": "Player1"
    }
    ```
5. Click **Send** to register the player. You should receive a response:
    ```json
    {
        "message": "Player Player1 registered successfully."
    }
    ```

### Step 3: Start a Game
1. Select `POST` in the request type dropdown.
2. Enter the URL: `http://127.0.0.1:5000/api/game/start`.
3. Go to the **Body** tab, select **raw**, and choose **JSON** format.
4. Enter the following JSON to start the game:
    ```json
    {
        "player1": "Player1",
        "player2": "Player2"
    }
    ```
5. Click **Send** to start the game. You should get the following response:
    ```json
    {
        "message": "Game started successfully between Player1 and Player2."
    }
    ```

### Step 4: Play a Round
1. Select `POST` in the request type dropdown.
2. Enter the URL: `http://127.0.0.1:5000/api/game/play_round`.
3. Go to the **Body** tab, select **raw**, and choose **JSON** format.
4. Enter the following JSON to play a round:
    ```json
    {
        "player1": "Player1",
        "player2": "Player2",
        "player1_choice": "rock",
        "player2_choice": "scissors"
    }
    ```
5. Click **Send**. The response will show the winner and the updated leaderboard:
    ```json
    {
        "message": "Player1 wins!",
        "leaderboard": {
            "Player1": {
                "games_won": 1,
                "score": 1
            },
            "Player2": {
                "games_won": 0,
                "score": 0
            }
        }
    }
    ```

### Step 5: Get the Leaderboard
1. Select `GET` in the request type dropdown.
2. Enter the URL: `http://127.0.0.1:5000/api/leaderboard`.
3. Click **Send** to retrieve the leaderboard. The response will look like this:
    ```json
    {
        "sorted_by_name": [
            ["Player1", {"games_won": 1, "score": 1}],
            ["Player2", {"games_won": 0, "score": 0}]
        ],
        "sorted_by_score": [
            ["Player1", {"games_won": 1, "score": 1}],
            ["Player2", {"games_won": 0, "score": 0}]
        ]
    }
    ```

## 4. Conclusion

This manual covers how to set up, interact with, and test the Rock-Paper-Scissors Tournament API using Postman. Follow the steps to register players, start games, play rounds, and view the leaderboard.
