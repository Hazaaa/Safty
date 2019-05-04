import cv2
import datetime
import os

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

ret, screenshot = cam.read()
cam.release()

savepath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures') #Change to any location you want
date = datetime.datetime.now()
fullpath = savepath + "\\" + date.strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"

cv2.imwrite(fullpath, screenshot)

cv2.destroyAllWindows()
