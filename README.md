<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guess Game README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            padding: 20px;
        }
        h1, h2 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>Guess Game</h1>

    <h2>Overview</h2>
    <p>This is a simple Number Guessing Game built using Flask for the backend and HTML, CSS, and JavaScript for the frontend. The game allows users to select a difficulty level and then guess a number within a specified range.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Select Difficulty:</strong> Choose between Easy, Medium, and Hard difficulty levels.</li>
        <li><strong>Guess Feedback:</strong> Get feedback on whether the guess is too high, too low, and if the guessed number is odd or even.</li>
        <li><strong>Persistent State:</strong> The game maintains the state of the range and the number to be guessed across requests.</li>
    </ul>

    <h2>Files</h2>

    <h3>Backend</h3>
    <ul>
        <li><code>app.py</code>: Main application file containing the Flask routes and logic.</li>
        <li><code>templates/index.html</code>: Main HTML file served to the user.</li>
        <li><code>static/style.css</code>: CSS file for styling the application.</li>
        <li><code>static/script.js</code>: JavaScript file for handling frontend logic and interactions.</li>
    </ul>

    <h2>How It Works</h2>
    <ol>
        <li><strong>Select Difficulty:</strong> The user selects a difficulty level from a dropdown menu.</li>
        <li><strong>Start Game:</strong> The user clicks the "Start Game" button which sends a POST request to the server to initialize the game with the selected difficulty.</li>
        <li><strong>Guess the Number:</strong> The user enters a guess and submits it. The server responds with feedback on whether the guess is correct, too high, or too low, and if the number is odd or even.</li>
        <li><strong>Feedback Display:</strong> The feedback is displayed to the user, guiding them to guess the correct number.</li>
    </ol>

    <h2>Setup Instructions</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone &lt;repository-url&gt;</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd guess-game</code></pre>
        </li>
        <li>Install the required dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Run the Flask application:
            <pre><code>flask run</code></pre>
        </li>
        <li>Open your browser and navigate to <code>http://127.0.0.1:5000</code> to start the game.</li>
    </ol>

    <h2>HTML and CSS Instructions</h2>

    <h3>HTML Structure</h3>
    <p><code>index.html</code>: The main HTML structure containing the game interface with difficulty selection and guess input sections.</p>

    <h3>CSS Styling</h3>
    <p><code>style.css</code>: Contains styles for the body, container, buttons, and inputs to enhance the visual appearance of the game.</p>

    <h3>JavaScript Interactions</h3>
    <p><code>script.js</code>: Handles user interactions, including starting the game and submitting guesses, by communicating with the Flask backend.</p>

    <h2>Contact</h2>
    <p>For any issues or questions, please open an issue in the repository or contact the project maintainer.</p>
</body>
</html>
