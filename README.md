# Playing Cards Detection using YOLOv5

## Introduction

The Playing Cards Detection project using YOLOv5 is a system for identifying and classifying playing cards using the YOLOv5n model.

<p align="center">
  <img src="https://raw.githubusercontent.com/vo-vuong/assets/main/playing_cards_detection-yolo/demo.png" width=300 height=400px><br/>
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
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate  # For Windows
```

4. Install submodule Yolov5:

```bash
git submodule init
git submodule update
```

5. Install the dependencies:

```bash
pip install -r yolov5/requirements.txt
```

6. Download the weight file at [best.pt](https://drive.google.com/file/d/14bZfjCO-y1K09V0_QgQcX_fiLjpCz7o5/view?usp=sharing) and move it to the root folder.
</details>

<details>
<summary>Inference</summary>

Run inferences on various sources and the results will be saved at `yolov5/runs/detect`.

```bash
python yolov5/detect.py --weights best.pt --hide-conf --source 0                               # webcam
                                                               img.jpg                         # image
                                                               vid.mp4                         # video
                                                               screen                          # screenshot
                                                               path/                           # directory
                                                               list.txt                        # list of images
                                                               list.streams                    # list of streams
                                                               'path/*.jpg'                    # glob
                                                               'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                                                               'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

</details>

## Additional Resources

- [Yolov5](https://github.com/ultralytics/yolov5)
- [Playing Cards Dataset](https://universe.roboflow.com/augmented-startups/playing-cards-ow27d)
