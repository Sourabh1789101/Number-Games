<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Number Guessing Game</title>
</head>
<body>

<h1>Number Guessing Game</h1>

<p>This is a Python-based number-guessing game with three difficulty levels: Easy, Medium, and Hard. Players try to think a randomly generated number, with the match providing hints if the guess is too high or too low. The game tracks the number of attempts and saves the best scores for each difficulty level.</p>

<h2>Features</h2>
<ul>
    <li>Three difficulty levels:
        <ul>
            <li>Easy: Guess a number between 1 and 10</li>
            <li>Medium: Guess a number between 1 and 50</li>
            <li>Hard: Guess a number between 1 and 100</li>
        </ul>
    </li>
    <li>Score tracking and saving of best scores</li>
    <li>Option to reset scores</li>
    <li>Display current best scores</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li><code>Flask</code> library</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository or download the code files.</li>
    <li>Install the <code>Flask</code> library if not already installed:
        <pre><code>pip install Flask</code></pre>
    </li>
</ol>

<h2>How to Run</h2>
<ol>
    <li>Ensure you have the required dependencies installed.</li>
    <li>Run the main script:
        <pre><code>python app.py</code></pre>
    </li>
    <li>Open your browser and navigate to <code>http://127.0.0.1:5000</code> to start the game.</li>
</ol>

<h2>File Structure</h2>
<ul>
    <li><code>app.py</code>: Main application file containing the Flask routes and logic.</li>
    <li><code>templates/index.html</code>: Main HTML file served to the user.</li>
    <li><code>static/style.css</code>: CSS file for styling the application.</li>
    <li><code>static/script.js</code>: JavaScript file for handling frontend logic and interactions.</li>
</ul>

<h2>Code Description</h2>
<ul>
    <li>The script initializes the Flask app and defines routes for starting the game and handling guesses.</li>
    <li>The <code>/start</code> route initializes the game with the selected difficulty level and sends the range to the frontend.</li>
    <li>The <code>/guess</code> route processes the user's guess and provides feedback on whether the guess is too high, too low, or correct.</li>
    <li>The <code>script.js</code> file handles the user interactions, such as starting the game and submitting guesses, by communicating with the Flask backend.</li>
</ul>

<h2>Main Menu Options</h2>
<ul>
    <li><strong>Easy</strong>: Starts the game in Easy mode.</li>
    <li><strong>Medium</strong>: Starts the game in Medium mode.</li>
    <li><strong>Hard</strong>: Starts the game in Hard mode.</li>
    <li><strong>Score</strong>: Displays the current best scores.</li>
    <li><strong>Reset</strong>: Resets the scores to default values.</li>
    <li><strong>Exit</strong>: Exits the game.</li>
</ul>

<h2>Example</h2>
<ol>
    <li>When you start the game, a menu will appear with options to select a difficulty level, view scores, reset scores, or exit.</li>
    <li>If you select a difficulty level, you will be prompted to guess a number within the specified range.</li>
    <li>The game will provide hints if your guess is too high or too low.</li>
    <li>Once you guess the correct number, the game will inform you of the number of steps taken and update the best score if applicable.</li>
    <li>You can choose to play again or exit.</li>
</ol>

<h2>Author</h2>
<p>This script was created by Sourabh kumar.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>

</body>
</html>
