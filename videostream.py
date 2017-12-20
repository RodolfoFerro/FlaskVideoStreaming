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
        face_cc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        success, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cc.detectMultiScale(gray, 1.3, 5)
        font = cv2.FONT_HERSHEY_SIMPLEX
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (180, 255, 10), 2)
            cv2.putText(image, 'Face detected!', (x + w//6, y - 15),
                        font, 0.003*w, (255, 180, 10), 2, cv2.LINE_AA)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
