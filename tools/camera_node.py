# Steps
# 1. Preparation (Setup)
# 2. The Infinite Observation Loop
# 3. Detection
# 4. The Report (Shipping the Data)

import cv2
import easyocr
import requests
import time

# configuration
API_URL = "http://127.0.0.1:8000/api/verification/capture/"
GATE_NAME = "Main Gate"

# Initialize EasyOCR Reader (English)
reader = easyocr.Reader(['en'])

def capture_and_process():
    # 0 = Default Laptop Webcam
    cap = cv2.VideoCapture(0)

    print(f"--- ALPR Node Active: Monitoring {GATE_NAME} ---")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Display the feed for your own monitoring
        cv2.imshow('Verimove Smart Gate Feed', frame)
        # Trigger Capture: In production, this would be motion detection.
        # For testing, press 's' to simulate a vehicle capture.
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            print("📸 Vehicle detected! Processing...")
            # 1. OCR Processing
            results = reader.readtext(frame)
            # Extract the first piece of text that looks like a plate
            plate_text = ""
            for (bbox, text, prob) in results:
                if prob > 0.4:
                    plate_text = text.strip()
                    break
            if plate_text:
                    print(f"🔍 Plate Detected: {plate_text}")
                    # 2. Convert frame to JPEG for transmission
                    _, buffer = cv2.imencode('.jpg', frame)
                    # 3. Ship to Django API
                    files = {'image': ('capture.jpg', buffer.tobytes(), 'image/jpeg')}
                    data = {'plate_number': plate_text, 'gate_name': GATE_NAME}
                    try:
                        response = requests.post(API_URL, files=files, data=data)
                        print(f"📡 API Response: {response.json()}")
                    except Exception as e:
                        print(f"❌ Connection Error: {e}")
            else:
                print("⚠️ No clear plate detected. Try again.")
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_process()