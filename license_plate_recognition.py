import cv2
import pytesseract


def recognize_license_plate(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(thresh, config='--psm 11')
    return text.strip()