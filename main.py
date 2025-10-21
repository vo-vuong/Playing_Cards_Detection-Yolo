import argparse
import os

from constants.config_const import THRESHOLD
from constants.paths_const import MODEL_FILE, TESTS_IMAGE_PATH, TRAINED_MODEL_PATH
from yolov11_detector import YOLOv11Detector


def get_args():
    parser = argparse.ArgumentParser(description="Test a YOLOv11 model")
    parser.add_argument(
        "--model", "-m", type=str, default=os.path.join(TRAINED_MODEL_PATH, MODEL_FILE)
    )
    parser.add_argument(
        "--test_images",
        "-i",
        type=str,
        default=os.path.join(TESTS_IMAGE_PATH, "img1.jpg"),
    )
    parser.add_argument("--threshold", "-t", type=float, default=THRESHOLD)

    return parser.parse_args()


def main():
    args = get_args()

    detector = YOLOv11Detector(
        model_path=args.model,
        conf_threshold=args.threshold,
    )

    print("Detecting on image...")
    detector.detect_image(args.test_images)


if __name__ == '__main__':
    main()
