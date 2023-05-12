import numpy as np
import skimage.morphology


def auto_median(image, footprint):
    # auto-median(I) = min(OCO(I), COC(I))

    image_oco = skimage.morphology.opening(
                    skimage.morphology.closing(
                        skimage.morphology.opening(image, footprint),
                        footprint),
                    footprint)
    image_coc = skimage.morphology.closing(
                    skimage.morphology.opening(
                        skimage.morphology.closing(image, footprint),
                        footprint),
                    footprint)

    image_auto_median = np.minimum(image_oco, image_coc)

    return image_auto_median
