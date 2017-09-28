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

    def get_frame(self):
        """
        Camera input for processing.
        """
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
