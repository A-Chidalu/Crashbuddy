from watson_developer_cloud import VisualRecognitionV3
import json
from app2 import *

visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_apikey='SOME_API_KEY')

with open(DOWNLOAD_DIRECTORY + '\\' + 'MMe33bbc6125fea20d238ecdc6fcb724d3.png', 'rb') as images_file:
        classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
        classifier_ids='CrashBuddy_800415549').get_result()
        print(json.dumps(classes, indent=2))

        jsonData = classes
        listData = jsonData['images']
        dictinfo = listData[0]
        classlist = dictinfo['classifiers'][0]['classes']
        # print(classlist)

        result = "This is most likely a " + classlist[0]['class'] + " with a likelihood of " + str(
            round(classlist[0]['score'] * 100)) + "%"

print(result)

