#import json
from watson_developer_cloud import VisualRecognitionV3
#import urllib
#import requests

def get_result(image_url):
    visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_apikey='SOME_API_KEY')

    with open(image_url, 'rb') as url:
        classes = visual_recognition.classify(
            url,
            threshold='0.54',
            classifier_ids='CrashBuddy_800415549').get_result()
    jsonData = classes
    listData = jsonData['images']
    dictinfo = listData[0]
    classlist = dictinfo['classifiers'][0]['classes']
    #print(classlist)

    result ="This is most likely a " + classlist[0]['class'] + " with a likelihood of " + str(round(classlist[0]['score'] * 100)) + "%"
    #print(result)
    #print(dictinfo)
    #print(json.dumps(classes, indent=2))

    return result

