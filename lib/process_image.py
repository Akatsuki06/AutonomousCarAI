

def process_img(intsarr,height,width,np,cv2):
    img = np.fromstring(intsarr, dtype='uint8')
    img.shape = (height,width,4)
    
    img = np.asarray(img)
    
    # cv2.imshow('Orginalimage',img)
    
    # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=img[250:384,0:512]
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # cv2.rectangle(img,(0,250),(512,384),(250,0,250),3)
    cv2.imshow('Final',img)
    # cv2.imshow('Gray',img)
#     img=cv2.GaussianBlur(img, (15, 15), 0)
#     cv2.imshow('Gaussian',img)
#     img=cv2.Canny(img,threshold1=50,threshold2=150)
#     # img = img[100:300, 0:100]
#     cv2.imshow('Canny',img)
    
#     lines = cv2.HoughLinesP(img, rho=1, theta=np.pi/180, threshold=20, minLineLength=20, maxLineGap=10)

#     for x1,y1,x2,y2 in lines[0]:
#         cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
 
    img = cv2.resize(img,(30, 30), interpolation = cv2.INTER_CUBIC)
    
    cv2.imshow('Final2',img)
    
    img=img.reshape(1,900)
    return img

