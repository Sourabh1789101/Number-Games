document.getElementById('start-game').addEventListener('click', function() {
    const difficulty = document.getElementById('difficulty').value;
    fetch('/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ difficulty: difficulty })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById('guess-section').style.display = 'block';
            document.getElementById('feedback').innerText = `Guess the number between ${data.range}`;
        }
    });
});

document.getElementById('submit-guess').addEventListener('click', function() {
    const guess = document.getElementById('guess').value;
    fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ guess: guess })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            let feedback = '';
            if (data.result === 'correct') {
                feedback = `Congratulations! You guessed the correct number in ${data.guesses} attempts.`;
            } else if (data.result === 'low') {
                feedback = 'Your guess is too low.';
            } else {
                feedback = 'Your guess is too high.';
            }
            feedback += ` Your guess is ${data.odd_or_even}.`;
            document.getElementById('feedback').innerText = feedback;
        }
    });
});
