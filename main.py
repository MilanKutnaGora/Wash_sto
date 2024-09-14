import cv2
import time
from face_detection import detect_face
from license_plate_recognition import recognize_license_plate
from gpio_control import CarWashComponents
from database import Database
from config import Config
from utils import setup_logging

logger = setup_logging()


def main():
    config = Config()
    db = Database(config.DB_CONFIG)
    car_wash = CarWashComponents()

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            logger.error("Failed to capture frame")
            continue

        face_detected = detect_face(frame)
        if face_detected:
            license_plate = recognize_license_plate(frame)
            if license_plate:
                logger.info(f"License plate detected: {license_plate}")

                if db.is_customer(license_plate):
                    start_car_wash(car_wash)
                else:
                    logger.info("New customer detected")
                    db.add_customer(license_plate)
                    start_car_wash(car_wash)

        time.sleep(0.1)

    cap.release()


def start_car_wash(car_wash):
    try:
        car_wash.activate_soap_pump(5)
        car_wash.activate_brush_motor(10)
        car_wash.activate_water_pump(15)
        car_wash.activate_dryer_fan(20)
    except Exception as e:
        logger.error(f"Error during car wash: {str(e)}")
    finally:
        car_wash.deactivate_all()


if __name__ == "__main__":
    main()