import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,400),cv2.FONT_HERSHEY_COMPLEX,1,(250, 201, 52))
cv2.putText(img,"Mercury",(90,250),cv2.FONT_HERSHEY_COMPLEX,0.7,(250, 201, 52))
cv2.putText(img,"Venus",(190,250),cv2.FONT_HERSHEY_COMPLEX,0.8,(250, 201, 52))
cv2.putText(img,"Earth",(290,260),cv2.FONT_HERSHEY_COMPLEX,0.8,(250, 201, 52))
cv2.putText(img,"Mars",(390,250),cv2.FONT_HERSHEY_COMPLEX,0.8,(250, 201, 52))
cv2.putText(img,"Jupiter",(520,300),cv2.FONT_HERSHEY_COMPLEX,1,(250, 201, 52))
cv2.putText(img,"Saturn",(800,300),cv2.FONT_HERSHEY_COMPLEX,1,(250, 201, 52))
cv2.putText(img,"Uranus",(960,300),cv2.FONT_HERSHEY_COMPLEX,1,(250, 201, 52))
cv2.putText(img,"Neptune ",(1100,300),cv2.FONT_HERSHEY_COMPLEX,1,(250, 201, 52))
cv2.imshow("output image",img)
cv2.waitKey(0)
cv2.imwrite("Planets_with_name.jpg",img)