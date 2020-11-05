from cv2 import cv2 as cv

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print (flags)