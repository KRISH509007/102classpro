import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    Number=random.randint(0,100)
    video_capture_object=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=video_capture_object.read()
        image_name="image"+str(Number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False 
    return image_name
    print("SnapShot Taken")    

 #To Close The Webcam..
    video_capture_object.release()
    cv2.destroyAllWindows()
   

def upload_file(image_name):
    access_token='Aw8y0IBSWroAAAAAAAAAAVFGE7NJmX92UaI_licT5lUOcgueOouOoTTohkdF09Oy'
    file=image_counter
    file_from=file
    file_to='/newfolder1/'+(image_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True)
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name) 

       
             
