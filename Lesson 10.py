import cv2
from PIL import Image

# img_path = 'cat.png'
img_path = 'cat1.jpg'

# cat_face = cv2.Cas

cat_face = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(img_path)
cat_f = cat_face.detectMultiScale(image)

okul = Image.open('okul.png')
cat = Image.open('cat1.jpg')
cat = cat.convert("RGBA")
okul = okul.convert("RGBA")

for (x,y,w,h) in cat_f:
    # cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,255), 3)
    okul = okul.resize((w, int(h/3)))
    cat.paste(okul, (x, y+int(h/3)))
    cat.save("cat_in_okul.png")
    c_o = cv2.imread("cat_in_okul.png")
    cv2.imshow("Cat", c_o)
    cv2.waitKey()