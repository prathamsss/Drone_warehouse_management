""" Utility to Generate, Read QR Code """
from tkinter.tix import Tree
import qrcode
import cv2
import ast

def generate_qr(name,data):
    """
    Mathod to generate QR With data
    :param name: Path of file to save/name
    :param val: data to be added
    :return: None (saves img)
    """
    img = qrcode.make(data)
    img.save( name + ".PNG")

def read_qr_stram(vid):
    """
    Method to QR Stram (Incomplete)
    :param vid: Video to pass
    :return: None
    """

    cap = cv2.VideoCapture(vid)
    d = cv2.QRCodeDetector()

    while (True):

        ret, frame = cap.read()
        a ,b , c = d.detectAndDecode(frame)
        print(a)

def read_qr_img(frame):
    """
    Method to read singe frame
    :param frame: img file path
    :return: data in QR
    """
    image  = cv2.imread(frame)
    d = cv2.QRCodeDetector()
    a, b, c = d.detectAndDecode(image)
    #out  = ast.literal_eval(a)
    return a


#generate_qr(path,val={f"Key_{i}" :i })


