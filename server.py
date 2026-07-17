from flask import Flask , render_template , request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detect():
    emotion = request.args.get('textToAnalyze')
    response = emotion_detector(emotion)

    if max(response, key=response.get):
        return "Invalid text! Please try again!."


    return (f"For the given statement, the system response is 'anger':{response['anger']},disgust: {response['disgust']} ,'fear':{response['fear']} 'joy':{response['joy']},'sadness':{response['sadness']}. The dominate emotion is {max(response , key=response.get)}")

@app.route('/')
def render_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5001)