import cv2


class Helpers:
    def __init__(self):
        pass

    """
    A helper function to resize an image to fit within a given size
    :param image: image to resize
    :param width: desired width in pixels
    :param height: desired height in pixels
    :return: the resized image
    """
    # Resizes a image and maintains aspect ratio
    def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
        # Grab the image size and initialize dimensions
        dim = None
        (h, w) = image.shape[:2]
        # Return original image if no need to resize
        if width is None and height is None:
            return image

        #resizing height if width is none
        if width is None:
            # Calculate the ratio of the height and construct the dimensions

            r = height / float(h)
            dim = (int(w * r), height)

        #resizing width if height is none
        else:
            
            # Calculate the ratio of the 0idth and construct the dimensions
            r = width / float(w)
            dim = (width, int(h * r))
            resized = cv2.resize(image, dim, interpolation=inter)
        
        # Return the resized image

        return resized

             

               

       

               

       


         

    

        
