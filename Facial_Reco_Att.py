import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

"""
USING TKINTER ADD/SHOW PHOTOS OF STUDENTS IN RECORD AND MARK TICK IF PRESENT ALONG WITH RECORDS
USE EXTERNAL CAMERA 
"""

# WEBCAM SELECTION
video_capture = cv2.VideoCapture(0)
if not video_capture:
    print("Cannot Open Camera")
    exit()

# LOAD  AND ENCODE KNOWN FACES
Swayam_image = face_recognition.load_image_file("FACES/SM.jpg")
Swayam_encoding = face_recognition.face_encodings(Swayam_image)[0]

Saqib_image = face_recognition.load_image_file("FACES/SAQ.jpg")
Saqib_encoding = face_recognition.face_encodings(Saqib_image)[0]

Sakshi_image = face_recognition.load_image_file("FACES/SAK.jpg")
Sakshi_encoding = face_recognition.face_encodings(Sakshi_image)[0]

Shrey_image = face_recognition.load_image_file("FACES/SH.jpg")
Shrey_encoding = face_recognition.face_encodings(Shrey_image)[0]

Anchal_image = face_recognition.load_image_file("FACES/AN.jpg")
Anchal_encoding = face_recognition.face_encodings(Anchal_image)[0]

Aarush_image = face_recognition.load_image_file("FACES/AR.jpg")
Aarush_encoding = face_recognition.face_encodings(Aarush_image)[0]

Yagesh_image = face_recognition.load_image_file("FACES/YAG.jpg")
Yagesh_encoding = face_recognition.face_encodings(Yagesh_image)[0]

Pallav_image = face_recognition.load_image_file("FACES/PAL.jpg")
Pallav_encoding = face_recognition.face_encodings(Pallav_image)[0]

Jatin_image = face_recognition.load_image_file("FACES/JA.jpg")
Jatin_encoding = face_recognition.face_encodings(Jatin_image)[0]


Nitin_image = face_recognition.load_image_file("FACES/NI.jpg")
Nitin_encoding = face_recognition.face_encodings(Nitin_image)[0]

known_face_encodings = [Swayam_encoding, Pallav_encoding, Yagesh_encoding, Jatin_encoding, Aarush_encoding, Satwik_encoding, Nitin_encoding, Shrey_encoding, Sakshi_encoding, Anchal_encoding, Saqib_encoding]
known_face_names = ['Swayam', 'Pallav', 'Yagesh', 'Jatin', 'Aarush', 'Satwik', 'Nitin', 'Shrey',  'Sakshi', 'Anchal', 'Saqib']

# LIST OF EXPECTED STUDENTS
Students = known_face_names.copy()


# face_locations = []
# face_encodings = []

# GET THE CURRENT DATE AND TIME

Now = datetime.now()
current_date = Now.strftime('%d-%m-%Y')

f = open(f'{current_date}.csv', 'a', newline='')
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # RECOGNIZE FACES
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for Face_Encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, Face_Encoding)  # RETURNS BOOLEAN IF MATCHES
        face_distance = face_recognition.face_distance(known_face_encodings, Face_Encoding)
        best_match_index = np.argmin(face_distance)  # MINIMUM CRITERIA SET
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # ADDS THE TEXT IF A PERSON IS PRESENT
        # global name
        if known_face_names[best_match_index] in known_face_names:
            font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
            BottomLeftCornerOfText = (10, 100)
            font_Scale = 1.5
            font_Colour = (255, 0, 0)
            thickness = 3
            line_type = 2
            cv2.putText(frame, known_face_names[best_match_index] + ' Present ', BottomLeftCornerOfText, font, font_Scale, font_Colour, thickness,
                        line_type)

            if known_face_names[best_match_index] in Students:  # REMOVING PRESENT STUDENTS FROM LIST
                Students.remove(known_face_names[best_match_index])
                current_time = Now.strftime('%H:%M:%S')
                lnwriter.writerow([known_face_names[best_match_index], current_time])

    cv2.imshow('Attendance', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # BREAKS LOOP ON PRESSING "q"
        break
video_capture.release()
cv2.destroyAllWindows()
f.close()
