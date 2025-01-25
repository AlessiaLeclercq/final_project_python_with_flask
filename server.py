"""
Emotion Detection Application using Python and Flask
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/")
def render_index_page():
    """
    Function that renders initial page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """ 
    Function that performs emotion detection task and renders results.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is not None:
        par = "<p>For the given statement, the system response is "
        par = par + f"""\"anger\": {response["anger"]}, """
        par = par + f"""\"disgust\": {response["disgust"]}, """
        par = par + f"""\"fear\": {response["fear"]}, """
        par = par + f"""\"joy\":{response["joy"]} and """
        par = par + f"""\"sadness\":{response["sadness"]}. """
        par = par + f"""The dominant emotion is <b>{response["dominant_emotion"]}</b>.</p>"""
    else:
        par = "<p>Invalid text! Please try again!</p>"
    return par


if __name__=="__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True
)
