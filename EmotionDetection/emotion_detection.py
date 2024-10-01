import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = obj, headers = header)

    formatted_res = json.loads(response.text)
    emotions = {}

    if response.status_code == 400:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        emotions = formatted_res['emotionPredictions'][0]['emotion']
        dominant_emotion = ''
        dominant_value = -1

        for emotion in emotions:    
            if emotions[emotion] > dominant_value:
                dominant_emotion = emotion
                dominant_value = emotions[emotion]

        emotions['dominant_emotion'] = dominant_emotion

    return emotions