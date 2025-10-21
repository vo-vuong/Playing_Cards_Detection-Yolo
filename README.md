# Playing Cards Detection using YOLOv11

## Introduction

The Playing Cards Detection project using YOLOv11 is a system for identifying and classifying playing cards using the YOLOv11 nano model.

<p align="center">
  <img src="https://raw.githubusercontent.com/vo-vuong/assets/main/playing_cards_detection-yolo/demo_yolov11_img1.jpg" width=320 height=320 style="display: inline-block; margin-right: 10px;">
  <img src="https://raw.githubusercontent.com/vo-vuong/assets/main/playing_cards_detection-yolo/demo_yolov11_img3.jpg" width=320 height=320 style="display: inline-block;">
  <br/>
  <i>playing cards demo</i>
</p>

<details>
<summary>Install</summary>

To install and run the project, follow these steps.

1. Clone the project from the repository:

```bash
git clone https://github.com/vo-vuong/Playing_Cards_Detection-Yolo.git
```

2. Navigate to the project directory:

```bash
cd Playing_Cards_Detection-Yolo
```

3. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # For Linux/Mac
.venv\Scripts\activate      # For Windows
```

4. Install submodule Yolov11:

```bash
git submodule init
git submodule update
```

5. Install the dependencies:

```bash
pip install -r requirements.txt
```

</details>

<details>
<summary>Inference</summary>

Run inferences on finetune model yolov11 nano the results will be saved at `outputs/images`.

```bash
python main.py --test_images `path/to/image` --threshold 0.6

Ex:
python main.py --test_images ./testing_images/img3.jpg --threshold 0.6
```

</details>

## Additional Resources

- [Yolo](https://github.com/ultralytics/ultralytics)
- [Playing Cards Dataset](https://universe.roboflow.com/augmented-startups/playing-cards-ow27d)
