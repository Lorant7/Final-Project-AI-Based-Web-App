"""
This module implements a Flask web application that detects emotions
from text input using the Watson NLP emotion detection service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")
@app.route("/emotionDetector")
def detect_emotion():
    """
    Detects the emotion from the provided text and returns the results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    result = "For the given statement, the system's response is "

    for emotion in emotions:
        if emotion != "dominant_emotion":
            result = result + str(emotion) + ": " + str(emotions[emotion])
    
    result = result + ". The dominant emotion is " + str(emotions['dominant_emotion'])
    return result

@app.route("/")
def render_index_page():
    """
    Renders the index page for the Emotion Detection application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
