import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime, timedelta
import pandas as pd


path = 'Training_images'
images = []
classNames = []
myList = os.listdir(path)
print("Files:", myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print("Names:", classNames)


def findEncodings(images):
    encodeList = []


    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name: str, marked: dict, half: str):
    now = datetime.now()
    dtString = now.strftime('%H:%M:%S')
    if name not in marked["Name"] and half == "first":
        dtString = now.strftime('%H:%M:%S')
        marked["Name"].append(name)
        marked["First Half"].append(dtString)
        marked["Second Half"].append("")
        print(name, "Marked First Half")
        pd.DataFrame.from_dict(marked).to_csv("Attendance.csv", index=False)

    elif name in marked["Name"] and half == "second":
        index = marked["Name"].index(name)
        if marked["Second Half"][index] == "":
            marked["Second Half"][index] = dtString
            print(name, "Marked Second Half")
            pd.DataFrame.from_dict(marked).to_csv("Attendance.csv", index=False)

encodeListKnown = findEncodings(images)
print('Encoding Complete')

marked = {"Name": [], "First Half": [], "Second Half": []}
# marked = {"Name": ["VISHWA"], "First Half": ["abc"], "Second Half": []}

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            

            first_half = datetime.now().replace(hour=5, minute=15, second=30, microsecond=0)
            # second_half = datetime.now().replace(hour=18, minute=25, second=30, microsecond=0)
            second_half = first_half + timedelta(seconds=10)
            duration = datetime.strptime("00:00:30", '%H:%M:%S')
            now = datetime.now()

            duration = first_half + timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)
            
            if now >= first_half and now < second_half:
                markAttendance(name, marked, "first")
            # elif now >= second_half and now < (now + timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)):
            elif now >= second_half and now < duration:
                markAttendance(name, marked, "second")

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
