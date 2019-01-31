import cv2

A = cv2.imread("icon.png", 1)
# cv2.imshow("A", A)
# cv2.waitKey(0)
print(A)
print(type(A))
print(A.ndim)