# import os

# import cv2
# DATA_DIR = './data'
# if not os.path.exists(DATA_DIR):
#     os.makedirs(DATA_DIR)
# number_of_classes = 3
# dataset_size = 100
# cap = cv2.VideoCapture(2)
# for j in range(number_of_classes):
#     if not os.path.exists(os.path.join(DATA_DIR, str(j))):
#         os.makedirs(os.path.join(DATA_DIR, str(j)))

#     print('Collecting data for class {}'.format(j))

#     done = False
#     while True:
#         ret, frame = cap.read()
#         cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
#                     cv2.LINE_AA)
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(25) == ord('q'):
#             break

#     counter = 0
#     while counter < dataset_size:
#         ret, frame = cap.read()
#         cv2.imshow('frame', frame)
#         cv2.waitKey(25)
#         cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

#         counter += 1

# cap.release()
# cv2.destroyAllWindows()

import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 10
dataset_size = 100
camera_index = 0  # Change this to the index of your camera (e.g., 0 for the default camera)

# Initialize video capture object
cap = cv2.VideoCapture(camera_index)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))
    print('Press "Q" to start collecting...')

    # Wait for user to press 'Q' to start collecting images
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" to start :)', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        
        # Check if frame is retrieved successfully
        if not ret:
            print("Error: Failed to retrieve frame.")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        
        # Save frame as image
        image_path = os.path.join(class_dir, '{}.jpg'.format(counter))
        cv2.imwrite(image_path, frame)
        
        counter += 1

cap.release()
cv2.destroyAllWindows()
