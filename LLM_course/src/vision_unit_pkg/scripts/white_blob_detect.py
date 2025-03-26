#!/usr/bin/env python3
import numpy as np
import cv2

class BlobDetect(object):
    def __init__(self, plot=True):
        self._plot = plot

    def plot_image(self,image, label=""):
        if self._plot:
            cv2.imshow(label, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def detect_large_white_blob(self, image, min_blob_size=10):
        """
        Detects white blobs in the image and marks them.
        Returns True if at least one large white blob is detected, otherwise False.
        """

        print(image.shape)
        # Check the number of channels in the image
        channels = image.shape[2] if len(image.shape) == 3 else 1

        # Convert the image to grayscale only if it's not already grayscale
        if channels == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            print("Grey Image...")
            gray = image
            
        
        gray = (gray * 255).astype(np.uint8)
        self.plot_image(gray, "grey")

        # Threshold the image
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        self.plot_image(binary, "binary_raw")
        binary = binary.astype(np.uint8)

        self.plot_image(binary, "binary")

        # Detect connected components (blobs)
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)

        # Flag to indicate the presence of a large blob
        has_large_blob = False
        print(image.shape)

        # Iterate over detected blobs
        for i in range(1, num_labels):
            x, y, w, h, size = stats[i]
            
            if size > min_blob_size:
                # Mark the blob on the image
                cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 2) 
                
                # Set flag to True
                has_large_blob = True

        return has_large_blob, image


def main():
    # Test the function
    path_img = "/LLM_course/src/vision_unit_pkg/scripts/init_image/blobtest.png"
    image = cv2.imread(path_img)

    obj = BlobDetect(plot=False)
    result, new_image = obj.detect_large_white_blob(image)

    if result:
        print("At least one large white blob detected!")
    else:
        print("No large white blobs detected.")

    # Show the marked image
    cv2.imshow('Marked Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()