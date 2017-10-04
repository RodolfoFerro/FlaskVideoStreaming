import cv2


class VideoStream():
    def __init__(self):
        """
        Constructor that returns a video camera input.
        """
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        """
        Class destructor.
        """
        self.video.release()

    def get_frame_grs(self):
        """
        Camera input for processing.
        Returns a grayscale image.
        """
        success, image = self.video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_frame_col(self):
        """
        Camera input for processing.
        Returns a color image.
        """
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def detect_faces(self):
        """
        Camera input for processing.
        Returns color image with face detection.
        """
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        success, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)     
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
