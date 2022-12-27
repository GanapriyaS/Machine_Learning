#Install the libraries 
#pip install opencv-python
#conda install -c conda-forge dlib
#pip install face_recognition

import cv2

#defing the variable and reading the file
img = cv2.imread("images/elon1.jfif")
#it is interpreting the image in BGR format 
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]


#accessing the image in the file from we have to match 
img2 = cv2.imread("images/elon2.jfif")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]


#For Matching the images for cases 
final_result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("final_result: ", final_result)
