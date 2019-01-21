class visa_photo(object):
    from PIL import Image
    import matplotlib.pyplot as plt
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # function to check the dimension of canvas
    def dim(self):
        print ('The dimension of the photo is (W X H): %d inch X %d inch' %(self.width, self.height))

    # function to print a photo to the empty canvas
    def print_photo(self, img, filename, dpi, actual_w = 2, actual_h = 2):
        # actual_h, actual_w: actual printed height and width (inch) for one photo
        ratio = actual_h / actual_w
        width, height = img.size
        center = [width / 2, height / 2]
        shorter_side = min(img.size)
        longer_side = max(img.size)
        if shorter_side * ratio <= longer_side:
            longer_side = shorter_side * ratio # ratio != 1 if the not print square photo
        # make a square photo from original one
        else:
            shorter_side = longer_side / ratio

        # crop the original photo
        img_crop = img.crop(
            (center[0] - shorter_side / 2,
            center[1] - longer_side / 2,
            center[0] + shorter_side / 2,
            center[1] + longer_side / 2
            )
        )
        w = self.width
        h = self.height
        ncol = int(w / actual_w) # calculate maximum numbers of rows and columns can print
        nrow = int(h / actual_h)

        w_space = (w - ncol*actual_w)/2/w
        h_space = (h - nrow*actual_h)/2/h
        fig, ax = plt.subplots(nrow, ncol, figsize = (w, h))
        for i in range(0, nrow):
            for j in range(0, ncol):
                ax[i,j].imshow(img_crop, aspect = 'auto', extent = (0, 1, 0, 1))
                ax[i,j].axis('off')
                ax[i,j].axhline(linewidth=0.3, color = 'black') # add border for each subplot
                ax[i,j].axvline(linewidth=0.3, color = 'black')
        fig.subplots_adjust(hspace = 0, wspace = 0, left = w_space, right = 1 - w_space, bottom = h_space, top = 1 - h_space)
        fig.savefig(filename, dpi = dpi)