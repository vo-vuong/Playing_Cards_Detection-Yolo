import sys
from pathlib import Path

from ultralytics import YOLO

from constants.paths_const import TEST_OUTPUT_PATH

sys.path.insert(0, str(Path(__file__).parent / 'yolov11'))


class YOLOv11Detector:

    def __init__(self, model_path='', conf_threshold=0.6):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold

    def detect_image(self, image_path, save_result=True, output_dir=TEST_OUTPUT_PATH):
        # Inference on image
        results = self.model.predict(
            source=image_path,
            conf=self.conf_threshold,
            save=save_result,
            project=output_dir,
        )

        return results
