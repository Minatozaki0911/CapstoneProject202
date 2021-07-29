import copy
import cv2
import numpy as np
from keras.models import load_model
import time
from urllib import request
import time

prediction = ''
score = 0
bgModel = None

URL='http://192.168.1.4:8080/shot.jpg'

gesture_names = {0: 'Nam Tay',
                 1: 'Chu L',
                 2: 'OK',
                 3: 'Chu V',
                 4: 'Ban tay'}

model = load_model('./Do_an_HK202_Model')
print("model loaded")

def predict_rgb_image_vgg(image):
    image = np.array(image, dtype='float32')
    image /= 255
    pred_array = model.predict(image)
    print(f'pred_array: {pred_array}')
    result = gesture_names[np.argmax(pred_array)]
    print(f'Result: {result}')
    print(max(pred_array[0]))
    score = float("%0.2f" % (max(pred_array[0]) * 100))
    print(result)
    return result, score

def remove_background(frame):
    fgmask = bgModel.apply(frame, learningRate=learningRate)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res

cap_region_x_begin = 0.5
cap_region_y_end = 0.8
threshold = 60
blurValue = 41
bgSubThreshold = 50
learningRate = 0

predThreshold= 95

isBgCaptured = 0

while True: 
    stream = np.array(bytearray(request.urlopen(URL).read()), dtype=np.uint8)
    frame = cv2.imdecode(stream, -1)
    #frame = cv2.resize(frame, (700,400))
    frame = cv2.bilateralFilter(frame, 5, 50, 100)
    frame = cv2.flip(frame, 1)

    cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
                  (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (0, 255, 0), 2)

    if isBgCaptured == 1:
        img = remove_background(frame)

        img = img[0:int(cap_region_y_end * frame.shape[0]),
              int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)

        cv2.imshow('GRAY IMAGE', cv2.resize(blur, dsize=None, fx=0.5, fy=0.5))

        ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        cv2.imshow('THRESHOLD IMAGE', cv2.resize(thresh, dsize=None, fx=0.5, fy=0.5))

        if (np.count_nonzero(thresh)/(thresh.shape[0]*thresh.shape[0])>0.2):
            if (thresh is not None):
                target = np.stack((thresh,) * 3, axis=-1)
                target = cv2.resize(target, (224, 224))
                target = target.reshape(1, 224, 224, 3)
                prediction, score = predict_rgb_image_vgg(target)

                print(score,prediction)
                if (score>=predThreshold):
                    cv2.putText(frame, "Sign:" + prediction, (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 3,
                                (125, 255, 0), 5, lineType=cv2.LINE_AA)
    thresh = None

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    elif key == ord('b'):
        bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)

        isBgCaptured = 1
        cv2.putText(frame, "Background captured", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 3,
                    (212, 0, 212), 5, lineType=cv2.LINE_AA)
        time.sleep(2)
        print('Background Reference')

    elif key == ord('r'):
        bgModel = None
        isBgCaptured = 0
        cv2.putText(frame, "Background reset", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 3,
                    (50, 0, 200), 5,lineType=cv2.LINE_AA)
        print('Background reference reset')
        time.sleep(1)

    cv2.imshow('From camera', cv2.resize(frame, dsize=None, fx=0.5, fy=0.5))

cv2.destroyAllWindows()
