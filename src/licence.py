import cv2
import os

# Load the Haar Cascade for license plate detection
plate_cascade = cv2.CascadeClassifier('haarcascade_licence_plate_rus_16stages.xml')

# Specify the path to the video file
video_path = 'motor.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Create a directory to save snapshots
output_dir = 'license_plates'
os.makedirs(output_dir, exist_ok=True)
count = 0

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect license plates
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

    # Draw rectangle around the license plates
    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('License Plate Detection', frame)

    # Check if the user pressed a key
    key = cv2.waitKey(30) & 0xFF
    if key == 27:  # Press 'ESC' to exit
        break
    elif key == ord('s'):  # Press 's' to save snapshot
        for (x, y, w, h) in plates:
            # Crop and save the detected plate
            plate = frame[y:y+h, x:x+w]
            filename = os.path.join(output_dir, f'plate_{count}.png')
            cv2.imwrite(filename, plate)
            print(f'Saved {filename}')
            count += 1

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
