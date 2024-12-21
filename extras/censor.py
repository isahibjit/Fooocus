import numpy as np

class Censor:
    def __init__(self):
        pass  # No need for initialization

    def censor(self, images: list | np.ndarray) -> list | np.ndarray:
        single = False
        if not isinstance(images, (list, np.ndarray)):
            images = [images]
            single = True

        # Directly return the input images as they are
        checked_images = images

        if single:
            checked_images = checked_images[0]

        return checked_images


default_censor = Censor().censor
