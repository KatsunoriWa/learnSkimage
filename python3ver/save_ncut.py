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
    import cv2
    oDir = pathlib.Path("out")
    if not oDir.is_dir():
       oDir.mkdir() 
    for p in pathlib.Path("../images").glob("*.png"):
        print(p)
        
        oname = oDir.joinpath(p.with_suffix(".jpg").name)
        img = io.imread(p)
        out, _ = plotNcut(img)
        io.imsave(str(oname), out)
        print(oname)

