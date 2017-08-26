

def process_img(intsarr,height,width,np,cv2):
    img = np.fromstring(intsarr, dtype='uint8')
    img.shape = (height,width,4)
    img = np.asarray(img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.Canny(img,threshold1=100,threshold2=300)
    cv2.imshow('processed_image',img)
    img = cv2.resize(img,(20, 20), interpolation = cv2.INTER_CUBIC)
    img=img.reshape(1,400)
    return img

