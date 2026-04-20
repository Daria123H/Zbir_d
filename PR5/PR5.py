import cv2
from PIL import Image
import numpy as np

path = r'd:\Збір даних\Пр5\Sunflower_from_Silesia2.jpg'


img = Image.open(path).convert("RGB")


image = np.array(img)
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
