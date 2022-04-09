import cv2
import numpy as np
im2=None
'''                 adjust options                      '''
def brightness_edit(value,tmp):
    hsv = cv2.cvtColor(tmp,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    lim = 255 - value
    v[v>lim] = 255
    v[v<=lim] += value
    final_hsv = cv2.merge((h,s,v))
    img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
    return img
    
def contrast_edit(value,tmp):
    Alpha = float(131 * (value + 127)) / (127 * (131 - value))
    Gamma = 127 * (1 - Alpha)
    img= cv2.addWeighted(tmp, Alpha,tmp,0, Gamma)
    return img

def blur_edit(value,tmp):
    value=value//10
    kernel_size = (value+1,value+1) # +1 is to avoid 0
    img = cv2.blur(tmp,kernel_size)    
    return img

'''                      filter options           '''
def bandw(img):
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    bw=cv2.cvtColor(blackAndWhiteImage,cv2.COLOR_BGR2RGB)
    return bw

def emboss(img):
    #inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return  sk_gray  

def grayscal(img1):
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.merge((gray,gray,gray))
    return img2    

def bleam(img1):
    sk_gray, sk_color = cv2.pencilSketch(img1, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return  sk_color

def leer(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return  hdr   

def sepia(img1):
    img = cv2.transform(img1, np.matrix([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]]))
    return img

def gaussian(img1):
    gaussian_blur = cv2.GaussianBlur(img1,(5,5),cv2.BORDER_DEFAULT)  
    return gaussian_blur        

def median(img1):
    median = cv2.medianBlur(img1,5)     
    return median                         

'''                       text options                     '''
def fontis(val):
    if val=='Pialo':
        fon=cv2.FONT_HERSHEY_SIMPLEX
    elif val=='Phoenix':
        fon=cv2.FONT_HERSHEY_PLAIN     
    elif val=='Reyna':
        fon=cv2.FONT_HERSHEY_DUPLEX  
    elif val=='MV Astra':
        fon=cv2.FONT_HERSHEY_COMPLEX  
    elif val=='Omen':
        fon=cv2.FONT_HERSHEY_TRIPLEX  
    elif val=='Yoru':
        fon=cv2.FONT_HERSHEY_COMPLEX_SMALL  
    elif val=='Cypher':
        fon=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  
    elif val=='Skye':
        fon=cv2.FONT_HERSHEY_SCRIPT_COMPLEX 
    return fon


def texter(img,val,font,textcol):
    def click_event(event, x, y, flags, params):
        global im2
        if event == cv2.EVENT_LBUTTONDOWN:
            im2=cv2.putText(img, val, (x,y), font,
                1, textcol, 2)
            cv2.imshow('image',im2)
                

    cv2.imshow('image', img)
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    # close the window
    cv2.destroyAllWindows()
    return im2
    
            
        
        
        
        
        
        
        
        
        
        
        