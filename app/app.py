import os
import random
from flask import Flask, render_template, request, jsonify, send_from_directory, url_for

app = Flask(__name__, static_folder='static')

# Game state
current_game = {
    'target': None,
    'min': None,
    'max': None,
    'guesses': 0
}

@app.route('/')
def index():
    script_version = str(int(os.path.getmtime(os.path.join(app.static_folder, 'script.js'))))
    style_version = str(int(os.path.getmtime(os.path.join(app.static_folder, 'style.css'))))
    return render_template('index.html', script_version=script_version, style_version=style_version)

@app.route('/start', methods=['POST'])
def start_game():
    difficulty = request.json.get('difficulty')
    if difficulty == 'easy':
        current_game['min'], current_game['max'] = 1, 10
    elif difficulty == 'medium':
        current_game['min'], current_game['max'] = 1, 50
    elif difficulty == 'hard':
        current_game['min'], current_game['max'] = 1, 100
    else:
        return jsonify({'error': 'Invalid difficulty'}), 400

    current_game['target'] = random.randint(current_game['min'], current_game['max'])
    current_game['guesses'] = 0
    return jsonify({'range': f"{current_game['min']} to {current_game['max']}"})

@app.route('/guess', methods=['POST'])
def check_guess():
    try:
        guess = int(request.json.get('guess'))
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid guess'}), 400

    current_game['guesses'] += 1

    if guess == current_game['target']:
        result = 'correct'
    elif guess < current_game['target']:
        result = 'low'
    else:
        result = 'high'

    odd_or_even = 'even' if guess % 2 == 0 else 'odd'

    return jsonify({
        'result': result,
        'guesses': current_game['guesses'],
        'odd_or_even': odd_or_even
    })

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
