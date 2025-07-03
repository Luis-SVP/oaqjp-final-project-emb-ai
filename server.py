''' Executing this function initiates the application of emtion
    detector to be executed over Flask deployed on localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package:
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the dominant emotion.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyse = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and get the response
    response = emotion_detector(text_to_analyse)

    # get the dominant emotion as a variable and remove it from the dictionary
    emotion = response["dominant_emotion"]
    response.pop("dominant_emotion", None)

    # drop the braces, replace the last "," with " and ", and construct the output sentence
    scores = str(response).replace("{", "").replace("}", "")
    parts = scores.rsplit(", ", 1)
    scores = " and ".join(parts)
    output = f"For the given statement, the system response is {scores}. The dominant emotion is {emotion}."

    return output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host='0.0.0.0', port=5000)
