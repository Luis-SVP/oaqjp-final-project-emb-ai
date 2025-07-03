"""
emotion)detection.py

Implements emotion analysis by calling IBM Watson NLP.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """ Analyze the emotion of the argument using a Watson NLP model."""
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json = input_json, headers=header, timeout=10)
    formatted_response = json.loads(response.text)

    # Obtain the emotions scores
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy'] 
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # get the dominant emotion
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    dominant_score = emotion_scores[dominant_emotion]

    # create the output format
    result = {'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return result
