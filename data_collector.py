import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImage"
img_name = "image"
img_grey = "grey"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']

number_of_images = 6

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

os.makedirs(IMAGE_PATH, exist_ok=True)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

     # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    imgname = os.path.join(IMAGE_PATH, img_name+'.'+'{}.jpg'.format(str(uuid.uuid1())))
    imggrey = os.path.join(IMAGE_PATH, img_grey+'.'+'{}.jpg'.format(str(uuid.uuid1())))

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(imgname, frame)
    cv2.imwrite(imggrey, gray)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    time.sleep(2)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# for label in labels:
#     img_path = os.path.join(IMAGE_PATH, label)
#     # if os.path.exists(img_path):

#     os.makedirs(img_path, exist_ok=True)

#     # Open camera
#     cap = cv2.VideoCapture(1)
#     print(f"Collecting images for {label}")
#     time.sleep(10)

#     for imgnum in range(number_of_images):
#         print(f"Collecting image number: {imgnum}")
#         ret, frame = cap.read()
#         imgname = os.path.join(IMAGE_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
#         cv2.imwrite(imgname, frame)
#         cv2.imshow('frame', frame)
#         time.sleep(2)

#         if cv2.waitKey(1) & 0xFF==ord('q'):
#             break

#     cap.release()
