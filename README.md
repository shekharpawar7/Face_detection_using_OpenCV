title: Face_detection_using_OpenCV
description: >
  A face recognition system is a technology capable of identifying or verifying a person from a digital image or a video frame from a video source. This system can be applied to various domains such as security systems, banking, attendance tracking, and personalized user experiences. Exploring OpenCV.

project_structure: |
```bash
  project_root/
  ├── dataset/
  │   ├── user_1.jpg
  │   ├── user_2.jpg
  │   └── ...
  ├── trainer/
  │   └── trainer.yaml
  ├── 01_face_dataset.py
  ├── 02_face_training.py
  ├── 03_face_detect.py
  ├── haarcascade_frontalface_default.xml
  └── README.md
```

usage_instructions: |
  step-by-step instructions on how to use your project:

  1. Prepare the dataset:
     ```bash
     python 01_face_dataset.py
     ```

  2. Train the model:
     ```bash
     python 02_face_training.py
     ```

  3. Run face detection:
     ```bash
     python 03_face_detect.py
     ```
applications:

  - Face Recognition in Security Systems: Enhance security by identifying individuals in restricted areas.
  - Biometric Authentication: Use face recognition for secure authentication in banking and other applications.
  - Attendance Systems: Automatically track attendance in classrooms or workplaces.

architecture:

![architecture_img](https://github.com/shekharpawar7/Face_detection_using_OpenCV/raw/main/architecture.png)

  phase_1: Face Detection
    steps:
      - Load Haar Cascade Classifier: The `haarcascade_frontalface_default.xml` file is used for detecting faces.
      - Capture the Image: OpenCV captures images from the Raspberry Pi camera module.
      - Preprocess the Image: Convert the captured image to grayscale to improve the efficiency of the face detection algorithm.
      - Save Detected Faces: Detected face regions are saved as grayscale images to create a dataset for training.
  
  phase_2: Model Training
    description: 
      The Local Binary Patterns Histograms (LBPH) algorithm is used for face recognition due to its robustness and simplicity. Grayscale face images captured in Phase 1 are used to train the model. The trained model is then saved for later use in real-time recognition.
  
  phase_3: Face Recognition
    steps:
      - Load Trained Model: The trained LBPH model is loaded.
      - Real-Time Recognition: The system captures frames from the camera, detects faces, and predicts the identity of the detected faces using the trained model.
      - Display Results: The system displays the recognized faces with confidence scores.

dataset_image: 

![Dataset 1 Image](https://github.com/shekharpawar7/Face_detection_using_OpenCV/raw/main/dataset1.png)
![Dataset 2 Image](https://github.com/shekharpawar7/Face_detection_using_OpenCV/raw/main/dataset2.png)

result: 

![Output Image](https://github.com/shekharpawar7/Face_detection_using_OpenCV/raw/main/output_1.png)
![Output Image](https://github.com/shekharpawar7/Face_detection_using_OpenCV/raw/main/output_2.png)



challenges_faced:

  - Data Quality and Quantity: Ensuring the dataset is large and diverse enough to capture different variations of faces.
  - Annotation Quality: Accurate labeling of faces in the images is crucial for model performance.
  - Class Imbalance: Addressing the imbalance in the number of images for each class (individual).
  - Overfitting: Ensuring the model generalizes well to unseen data.
  - Hardware Limitations: Training the model on devices with limited computational resources.

req :- opencv-contrib-python
       opencv-python
       numpy
