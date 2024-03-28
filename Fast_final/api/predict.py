import subprocess
import cv2
import os
os.chdir("../yolov8/ultralytics/yolo/v8/segment/")

def run_yolov5_detection(source):

    command = [
        "python", "predict_detect.py",
        "model=best.pt",
        f"source={source}"

    ]


    try:
        # Run the YOLOv5 detection command
        subprocess.run(command, check=True)
        return "proceso_ejecutado"

    except subprocess.CalledProcessError as e:
        return f"Error executing YOLOv5 detection: {e}"


if __name__ == "__main__":
    # Specify the path to the YOLOv5 weights file (yolov5s.pt)
    #pesos manual en step 1
    #yolov5_weights_path = "../yolov5/runs/train/exp/weights/best.pt"

    # Specify the source for detection (e.g., webcam: 0 or video file: "path/to/video.mp4")
    detection_source = "../datasets/pcb_dataset/images/val2023/11_missing_hole_02.jpg"

    # Run YOLOv5 detection
    run_yolov5_detection(detection_source)

    #breakpoint()
    #cv2.imshow('Imagen', image_final)
    #breakpoint()
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

#python detect.py --weights yolov5s.pt --source 0
#python detect.py --weights runs/train/exp8/weights/best.pt --source ../datasets/pcb_dataset/images/val2023/11_missing_hole_01.jpg
#Results saved to ../yolov5/runs/detect/exp2
#uvicorn api:app --reload
# python train.py --batch 16 --cfg cfg/training/custom_yolov7.yaml --epochs 15 --data data/custom.yaml --weights 'yolov7.pt'
#python train.py --img 640 --epochs 15 --data coco_custom.yaml --weights yolov5s.pt
