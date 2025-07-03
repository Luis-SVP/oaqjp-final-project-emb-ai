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
    return response.text
