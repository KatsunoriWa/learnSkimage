# -*- coding: utf-8 -*-
# pylint: disable=C0103
import pathlib
from skimage import io, segmentation, color
from skimage.future import graph

def plotNcut(img):
    """
    img: color img

    """

    labels1 = segmentation.slic(img, compactness=30, n_segments=400)
    g = graph.rag_mean_color(img, labels1, mode='similarity')
    labels2 = graph.cut_normalized(labels1, g)
    return color.label2rgb(labels2, img, kind='avg'), labels2

if __name__ == "__main__":

    for p in pathlib.Path(".").glob("**/*.png"):
        print(p)
        
        img = io.imread(p)
        out, _ = plotNcut(img)
        io.imshow(out)
        io.show()
