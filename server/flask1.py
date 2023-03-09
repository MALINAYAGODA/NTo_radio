import json
from pprint import pprint

import numpy as np
from flask import Flask, request
import cv2

def take_photo(msg):
    list_res = list(map(int, msg.split(';')[:-1]))
    frames = np.resize(np.array(list_res, dtype=float), (480, 640, 3))
    cv2.imshow('image', frames)
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    dct_robot = request.get_json(force=True)
    take_photo(dct_robot["camera"])
    dct = json.loads(open('json.json', 'r', encoding="utf-8").read())
    return dct

if __name__ == "__main__":
   app.run(host = 'localhost')
