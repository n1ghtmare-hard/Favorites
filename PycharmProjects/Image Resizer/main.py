import cv2

source = "istockphoto-1133604495-170667a.jpg"
output1 = "new image.png"
scale_percent = 50

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)


new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)


output = cv2.resize(image, (new_width, new_height))

cv2.imwrite(output1, output)
# cv2.waitKey(0)
