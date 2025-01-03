
# **Face Recognition Attendance System**

This project is a **Face Recognition-based Attendance System** that automates attendance tracking using real-time facial recognition. It uses a webcam to detect and recognize faces, marking attendance and logging details in a CSV file.

---

## **Features**
- **Real-time Face Recognition**: Utilizes a webcam for live face detection and recognition.
- **Automated Attendance Logging**: Recognizes individuals and records their names and timestamps in a CSV file.
- **Customizable Face Database**: Easily add or update face data for new individuals.
- **Exportable Attendance Records**: Saves daily attendance logs in CSV format with date-specific filenames.
- **Planned GUI Integration**: Upcoming features include adding photos, viewing records, and managing the system via a graphical interface (Tkinter).

---

## **Requirements**

### **Python Libraries**
Ensure the following libraries are installed:
- **`face_recognition`**: For face detection and recognition.
- **`opencv-python`**: For webcam access and video processing.
- **`numpy`**: For handling numerical computations.
- **`csv` and `datetime`**: For attendance logging and timestamping (built-in libraries).

Install required libraries:
```bash
pip install face_recognition opencv-python numpy
```

### **System Requirements**
- A working webcam (internal or external).
- Python 3.7 or newer.
- `dlib` library (automatically installed with `face_recognition`).

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/face-recognition-attendance-system.git
cd face-recognition-attendance-system
```

### **2. Prepare the Face Database**
- Create a folder named `FACES` in the project directory.
- Add images of individuals in the `FACES` folder. Name the files after the individuals (e.g., `John.jpg`, `Jane.jpg`).

### **3. Run the Script**
Execute the program:
```bash
python attendance_system.py
```

### **4. Attendance Logging**
- The system will recognize faces in real-time and display the names on the video feed.
- Attendance records will be saved in a CSV file named after the current date (e.g., `2024-11-22.csv`).

---

## **How It Works**

1. **Face Encoding**:
   - Reads images from the `FACES` folder.
   - Converts faces into numerical encodings for recognition.

2. **Real-time Detection**:
   - Captures live video feed using OpenCV.
   - Detects faces and matches them with the encoded database.

3. **Attendance Logging**:
   - Marks recognized individuals as "Present" with timestamps.

4. **Live Feedback**:
   - Displays recognized names on the video feed.

---

## **Customization**

### **Add New Faces**
1. Add clear, high-quality photos of individuals to the `FACES` folder.
2. Restart the program to update face encodings automatically.

### **Change Webcam Source**
- Modify the camera source in the code:
  ```python
  video_capture = cv2.VideoCapture(0)
  ```

Replace `0` with the appropriate index for your webcam.

---

## **Controls**
- **Press 'q'**: Stop the program and save attendance.

---

## **Future Enhancements**
- GUI for user-friendly interaction (add/view photos, records, etc.).
- Liveness detection to prevent spoofing using photos/videos.
- Integration with a database for scalable record management.
- Notifications (Email/SMS) for attendance updates.
- Web or mobile-based deployment.

---

## **Troubleshooting**

### **Common Errors**
1. **`ModuleNotFoundError: No module named 'face_recognition'`**
   - Install the library with:
     ```bash
     pip install face_recognition
     ```

2. **Camera Not Opening**
   - Ensure the webcam is properly connected and accessible by the system.

3. **Unrecognized Faces**
   - Ensure that:
     - Images in the `FACES` folder are clear and well-lit.
     - The system is trained with multiple images of the same person for better accuracy.

---

## **License**
This project is licensed under the **MIT License**. You are free to use, modify, and distribute the project.

---

## **Acknowledgments**
- **[face_recognition Library](https://github.com/ageitgey/face_recognition)**: Provides the core face recognition functionality.
- **OpenCV**: Enables real-time video processing.

---

Feel free to contribute to the project by submitting issues or pull requests!
