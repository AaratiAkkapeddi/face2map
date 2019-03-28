'''
========================
Face Vector to Topographic Map
========================

'''


import sys
import matplotlib
import face_recognition
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import math
import os

def group(lst, n):
  for i in range(0, len(lst), n):
    val = lst[i:i+n]
    if len(val) == n:
      yield tuple(val)

def write_face(filename):
    face = face_recognition.load_image_file(filename)
    try:
        gotdata = face_recognition.face_encodings(face)[0]
        face_encoding = face_recognition.face_encodings(face)[0]
        print(face_encoding)
        encoding = list(group(face_encoding, 4))
        x = []
        y = []
        z = []
        for i in encoding:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2] * i[3] * 100)
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1, projection='3d')
        ax._axis3don = False
        ax.tricontour(x, y, z,15, linewidths=[0.5], colors='k')
        ax.view_init(azim=0, elev=90)
        plt.axis([-0.08,0.08,-0.08,0.08])
        plt.show()
     

    except IndexError:
        print('no-face')


print(sys.argv[1])
write_face(sys.argv[1])


