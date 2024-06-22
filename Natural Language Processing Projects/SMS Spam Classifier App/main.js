function predictSpam() {
    const messageInput = document.getElementById('message').value;
    // Perform AJAX request or other logic to get prediction
    const prediction = getPrediction(messageInput);

    // Display prediction
    const resultSection = document.getElementById('resultSection');
    const predictionText = document.getElementById('predictionText');
    predictionText.innerText = prediction;
    resultSection.style.display = 'block'; // Show result section
}

// Mock function, replace with actual prediction logic
function getPrediction(message) {
    // Add your machine learning prediction logic here
    // For now, it returns a random prediction
    const predictions = ['Spam', 'Not Spam'];
    return predictions[Math.floor(Math.random() * predictions.length)];
}
