

def process_img(intsarr,height,width,np,cv2):
    img = np.fromstring(intsarr, dtype='uint8')
    img.shape = (height,width,4)
    
    img = np.asarray(img)
    
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 
    img = cv2.resize(img,(30, 30), interpolation = cv2.INTER_CUBIC)
    
    return img #a numpy array 30x30x3

