import cv2

image = cv2.imread("img.jpg")
blurry_image = cv2.medianBlur(image, 9)

laplacian = cv2.Laplacian(blurry_image, cv2.CV_64F).var()

if laplacian < 500:
    print("Blurry Image")

else:
    print("Not Blurry")

