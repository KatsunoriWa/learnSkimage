# -*- coding: utf-8 -*-
# pylint: disable=C0103
from skimage import data, io, segmentation, color
from skimage.future import graph
from matplotlib import pyplot as plt

def plotNcut(img):
    labels1 = segmentation.slic(img, compactness=30, n_segments=400)
    out1 = color.label2rgb(labels1, img, kind='avg')

    g = graph.rag_mean_color(img, labels1, mode='similarity')
    labels2 = graph.cut_normalized(labels1, g)
    out2 = color.label2rgb(labels2, img, kind='avg')

    plt.figure(1)
    io.imshow(out1)
    plt.figure(2)
    io.imshow(out2)
    io.show()

if __name__ == "__main__":
    import cv2
    import glob
    for name in glob.glob("*/*.png"):
        img = cv2.imread(name)[:, :, ::-1]
        plotNcut(img)
    #    cv2.waitKey(100)

