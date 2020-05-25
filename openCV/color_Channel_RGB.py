
import cv2
flag = 1
if(flag==0):

    image = cv2.imread("9D194DF8-01FE-4E4E-8AE0-522C77143077.jpg", cv2.IMREAD_UNCHANGED)
    img_b,img_g,img_r=cv2.split(image)
    cv2.imshow("b",img_b)
    cv2.imshow("g",img_g)
    cv2.imshow("r",img_r)
    cv2.waitKey(0);

    #왜 안되지? 그림 3개 나와야하는데..

if(flag==1) :
    import cv2

    image = cv2.imread("D:/test_img/Tulips.jpg", cv2.IMREAD_UNCHANGED)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(image)
    cv2.imshow("H", H)
    cv2.imshow("S", S)
    cv2.imshow("V", V)
    cv2.waitKey(0);
