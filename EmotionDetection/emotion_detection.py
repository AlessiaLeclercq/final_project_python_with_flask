import json
import requests

def find_max_index(scores:list):
    max_score, max_index = None, None
    for i, s in enumerate(scores):
        if max_score is None or s>max_score:
            max_score, max_index = s,i
    return max_index

def emotion_detector(text_to_analyse:str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=url, headers=headers, json=input_json)

    if response.status_code == 400:
        keys, values =["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"], [None, None, None, None, None, None]
    else:
        formatted_response = json.loads(response.text)
        keys = list(formatted_response["emotionPredictions"][0]["emotion"].keys())
        keys.append("dominant_emotion")
        values = list(formatted_response["emotionPredictions"][0]["emotion"].values())
        values.append(keys[find_max_index(values)])

    return dict(zip(keys, values))


