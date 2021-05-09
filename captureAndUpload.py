import cv2
import dropbox
import time 
import random 
# to get the start time 
start_time = time.time()

def take_snapshot():
    number = random.randint (0,100)
    #initialise cv2 for switching on the camera
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frame while camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device 
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False 

    return img_name 
    print("snapshot taken")
    #release the camera 
    videoCaptureObject.release()
    #close all the windows that might be opened for this process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.AwfMQkeRkO7qgtWvyfdnI6l6QlV3Lbyvh1SS832Evhwqg-dVd4bjodIqqC1EziiuftD61rP35DEBj6Z6e2QfFp2bpycQQnoDdlv0eusEB6drroXUMnFV8jag33lUjeWKIoja6M8"
    file = img_name
    file_from = file 
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main ():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)

main()