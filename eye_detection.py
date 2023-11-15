# face & Eye detection

# imports
import cv2

class Person:
    def __init__(self, face, eyes):
        self.face = face
        self.right_eye = Eye(eyes[0])
        self.left_eye = Eye(eyes[1])
    def check_states(self, eyes):
        l = len(eyes)
        if l ==  2:
            self.right_eye.update(eyes[0])
            self.left_eye.update(eyes[1])
            return (1,1)
        elif l == 1:
            self.right_eye.check_state(eyes[0])
            self.left_eye.check_state(eyes[0])
            return (self.right_eye.state, self.left_eye.state)
        else:
            return (0,0)

class Eye:
    def __init__(self, loc):
        self.location = loc
        self.previous = None
        self.state = 1
    def update(self, new_loc):
        self.previous = self.location
        self.location = new_loc
        self.state = 1
    def check_state(self, loc):
        if abs(loc[0] - self.location[0]) > 20:
            self.state = 0


def eye_identifier():
    """
    steps:
    1. face and eye detection: opencv
    2. determining closed open states for each eye
    3. relaying information
    
    inputs: None
    outputs: Left & Right eye states (tuple or class), face image & eye 
    images for mouse prediction model
    """
    user = None
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eyes_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: could not open camera")
        exit()
    while cap.isOpened():
        _, img = cap.read()
        result = face_and_eye_detector(img, face_cascade, eyes_cascade)
        if result:
            cv2.imshow('img', result[0])
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if user is None:
                if len(result[2]) == 2:
                    user = Person(result[1], result[2])
            else:
                print(user.check_states(result[2]))
    cap.release()

    

def face_and_eye_detector(img, face_model, eye_model):
    """
    Locates eyes and face from input image

    inputs: image
    outputs: eyes and face locations

    """

    ###### Need to eliminate bad faces and bad eye boxes #######

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_model.detectMultiScale(gray, 1.1, 4)
    if len(faces) != 0:
        face = faces[0]
        roi_gray = gray[face[1]:face[1]+face[3], face[0]:face[0]+face[2]]
        eyes = eye_model.detectMultiScale(roi_gray)  
        cv2.rectangle(img, (face[0],face[1]), (face[0]+face[2], face[1]+face[3]), (255, 0, 0), 3)
        roi_color = img[face[1]:face[1]+face[3], face[0]:face[0]+face[2]]
        new_eyes = false_eye_eliminator(eyes)
        for (ex, ey, ew, eh) in new_eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)
        return img, face, new_eyes
    else:
        return None
    
def false_eye_eliminator(eyes):
    """
    Takes in the eyes detected and eliminates items that are not eyes based on y location
    """
    eyes = sorted(eyes, key=lambda eye: eye[1], reverse=True)
    l = len(eyes)
    if l >= 3:
        diff_1 = abs(eyes[-1][2]**2 - eyes[-2][2]**2)
        diff_2 = abs(eyes[-3][2]**2 - eyes[-2][2]**2)
        if diff_1 < diff_2:
            real_eyes = sorted(eyes[len(eyes)-2:], key=lambda eye: eye[0])
        else:
            num = len(eyes)-3
            real_eyes = sorted(eyes[num:num+2], key=lambda eye: eye[0])
    else:
        real_eyes = sorted(eyes, key=lambda eye: eye[0])
    
    return real_eyes



if __name__ == "__main__":
    eye_identifier()
