import numpy as np
import cv2
import os
import sys
import time
from matplotlib import pyplot as plt



class Annotate:
    def __init__(self, filename_ext):
        self.filename_ext = filename_ext
        self.filename = filename_ext[:len(self.filename_ext) - 4]  # remove .avi
        self.frame = None
        self.count = 1

    def process_video(self):
        video = cv2.VideoCapture(self.filename_ext)
        print('loaded video {}'.format(self.filename))

        cv2.namedWindow('video {}'.format(self.filename))

        ter, lastFrame = video.read()
        lastFrame = cv2.cvtColor(lastFrame, cv2.COLOR_BGR2GRAY)
        frame_number =   1
        while video.isOpened():
            ret, self.frame = video.read()
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

            if not ret:
                break

            #we can modify self.frame here and it will show up!
            diff = cv2.absdiff(self.frame, lastFrame)

            #use diff
            #filter out non black objects


            #grayscale

            #what do I need to do to get data to sami

            #apply threashold
            #calculate number of non zeros
            #if number is above another threashold
                #framecount ++

            #return framecount and weather it is in the set


            lastFrame = self.frame
            subframe = diff[200:201, 0:1920]

            thresh = 127
            v_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

            print(np.average(subframe))
            cv2.imshow('window', diff)
            cv2.imshow('video {}'.format(self.filename), subframe)

            key = cv2.waitKey(0) & 0xFF
            if key == ord('h'):
                 plt.hist(subframe.ravel(), 256, [0, 256])
                 plt.show()

            elif key == ord('q'):
                 exit()

            frame_number += 1

        cv2.destroyAllWindows()


if __name__ == '__main__':
    a = Annotate(sys.argv[1])
    a.process_video()
