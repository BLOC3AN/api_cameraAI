import easyocr
import cv2
import os
from lib_detection import load_model, detect_lp, im2single
global graph
import matplotlib.pyplot as plt

reader = easyocr.Reader(['vi', 'en'])
wpod_net_path = "./models/wpod-net_update1.json"
wpod_net = load_model(wpod_net_path)

def process_image(image_path):
    Ivehicle = cv2.imread(image_path)

    Dmax = 608
    Dmin = 288

    ratio = float(max(Ivehicle.shape[:2])) / min(Ivehicle.shape[:2])
    side = int(ratio * Dmin)
    bound_dim = min(side, Dmax)
    _, LpImg, lp_type = detect_lp(wpod_net, im2single(Ivehicle), bound_dim, lp_threshold=0.5)

    if LpImg:
        image_rgb = cv2.cvtColor(LpImg[0], cv2.COLOR_BGR2RGB)
        temp_image_path = "static/temp.png"
        # cv2.imwrite(temp_image_path, image_rgb)
        fig = plt.figure()
        plt.imshow(image_rgb)
        plt.axis('off')
        fig.savefig(temp_image_path)
        reader_img = reader.readtext(temp_image_path, detail=0, paragraph=True)
        plt.close(fig)
        if reader_img:
            return reader_img[0]
    
    return None

def clean_temp_image():
    temp_image_path = "static/temp.png"
    if os.path.exists(temp_image_path):
        os.remove(temp_image_path)