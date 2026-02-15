import cv2
import numpy as np

def create_sample_image():
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    cv2.rectangle(img, (100, 100), (400, 400), (0, 255, 0), 3)
    cv2.putText(img, 'OpenCV', (150, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
    return img
try:
    img = cv2.imread('image.jpg')
    if img is None:
        img = create_sample_image()
        print("No image found, showing sample image")
except:
    img = create_sample_image()
    print("Showing sample image")

cv2.imshow('Image Window', img)
print("Press any key to close")

cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(1, 5):
    cv2.waitKey(1)