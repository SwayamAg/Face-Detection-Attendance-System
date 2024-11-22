### **README.md**

---

# **Face Recognition Attendance System**

This project is a **Face Recognition-based Attendance System** that uses a webcam to recognize faces and mark attendance automatically. It also supports real-time tracking and generates attendance records in CSV format.

---

## **Features**
- **Real-time Face Recognition**: Detects and recognizes faces using a webcam.
- **Automated Attendance**: Marks attendance for recognized individuals and logs their details (name and time) in a CSV file.
- **Customizable Face Database**: Add or update student photos for face encoding.
- **GUI Integration (Optional)**: Plan to integrate features like adding photos, viewing attendance records, and camera control using Tkinter.
- **Exportable Records**: Saves daily attendance records in a CSV file.

---

## **Requirements**

### **Python Libraries**
Make sure the following Python libraries are installed:
- `face_recognition`: For face detection and recognition.
- `opencv-python`: For webcam access and real-time video processing.
- `numpy`: For handling mathematical operations.
- `csv`: For saving attendance records.
- `datetime`: For timestamping attendance.

Install the required libraries with:
```bash
pip install face_recognition opencv-python numpy
```

### **System Requirements**
- A working webcam (external or built-in).
- Python 3.7 or above.
- `dlib` library for face encoding (automatically installed with `face_recognition`).

---

## **Setup Instructions**

### 1. **Clone or Download the Repository**
```bash
git clone https://github.com/your-username/face-recognition-attendance-system.git
cd face-recognition-attendance-system
```

### 2. **Prepare the Face Database**
- Create a folder named `FACES` in the project directory.
- Add images of individuals in the `FACES` folder with filenames corresponding to their names (e.g., `John.jpg`, `Jane.jpg`).

### 3. **Run the Script**
Run the script in your terminal:
```bash
python attendance_system.py
```

### 4. **Mark Attendance**
- The system will recognize faces in real-time via the webcam.
- Recognized individuals will be marked "Present" in a CSV file named with the current date (e.g., `22-11-2024.csv`).

---

## **Project Workflow**
1. **Face Encoding**:
   - The system loads images from the `FACES` folder.
   - Encodes faces into a numerical representation for recognition.

2. **Real-time Detection**:
   - Captures video feed using OpenCV.
   - Detects and recognizes faces in the video feed.

3. **Attendance Logging**:
   - Matches detected faces with known encodings.
   - Logs recognized individuals with the timestamp in a CSV file.

4. **Live Updates**:
   - Displays recognized names and attendance status on the video feed.

---

## **Customization**

### **Add New Students**
1. Add the student's photo to the `FACES` folder.
2. Update the `known_face_encodings` and `known_face_names` lists in the code.

### **Change Webcam Source**
- To use an external camera, change:
  ```python
  video_capture = cv2.VideoCapture(0)
  ```
  Replace `0` with the appropriate camera index.

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
