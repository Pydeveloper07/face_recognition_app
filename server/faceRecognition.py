#pip install --upgrade azure-cognitiveservices-vision-face
import pickle
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

KEY = "8ffb40fd80a74f66a7edcd5165a2fd3c"
ENDPOINT = "https://goodbye.cognitiveservices.azure.com/"
PERSON_GROUP_ID = "face_group"
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

with open('StudentID.pickle', 'rb') as handle:
    dicStudents = pickle.load(handle)

def face_recognition(photoLoc):
    image = open(photoLoc, 'r+b')
    face_ids = []
    face = face_client.face.detect_with_stream(image, detectionModel='detection_02')
    if not face:
        return "no"
    face = face[0]
    face_ids.append(face.face_id)
    person = face_client.face.identify(face_ids, PERSON_GROUP_ID)
    if not person:
        return "no"
    person = person[0]
    if len(person.candidates) > 0:
        name = dicStudents[person.candidates[0].person_id]
        print('Person: {} | Confidence: {}'.format(name, person.candidates[0].confidence))
        return name
    else:
        return "no"