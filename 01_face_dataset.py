import cv2
import os

# Initialize video capture and face detector
cam = cv2.VideoCapture(0)
cam.set(3, 1080)  # Set video width
cam.set(4, 550)  # Set video height

# Load the Haar cascade for face detection
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_detector.empty():
    print("Error loading Haar cascade file")
    exit()

# Ensure dataset directory exists
if not os.path.exists('dataset'):
    os.makedirs('dataset')

# Get user ID
while True:
    face_id = input('\nEnter user ID and press <return> ==>  ')
    if face_id.isdigit():
        face_id = int(face_id)
        break
    else:
        print("Please enter a numeric value for user ID.")

print("\n[INFO] Initializing face capture. Look at the camera and wait...")

# Initialize face count
count = 0
while True:
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    img = cv2.flip(img, 1)  # Flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Print image shapes for debugging
    print(f"Image shape: {img.shape}")
    print(f"Gray image shape: {gray.shape}")

    # Detect faces in the image
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) == 0:
        print("No faces detected")
    else:
        print(f"Faces detected: {len(faces)}")
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        face_image = gray[y:y + h, x:x + w]
        filename = f"dataset/User.{face_id}.{count}.jpg"
        if cv2.imwrite(filename, face_image):
            print(f"Image saved: {filename}")
        else:
            print(f"Failed to save image: {filename}")
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 500:  # Take 70 face samples and stop
        break

# Cleanup
print("\n[INFO] Exiting Program and cleaning up...")
cam.release()
cv2.destroyAllWindows()
