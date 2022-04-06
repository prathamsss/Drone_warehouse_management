from tkinter.tix import Tree
import qrcode
import cv2

def generate_qr(name,val):
    img = qrcode.make(val)
    img.save( name + ".PNG")
 
def read_qr(vid):

    cap = cv2.VideoCapture(vid) 
    d = cv2.QRCodeDetector()

    while (True):
        
        ret, frame = cap.read()
        a ,b , c = d.detectAndDecode(frame)
        print(a)
