#Detection of Pornographic Digital Images
#YCbCr Model
#author:Robin chen
#input:the dir of an image
'''
ref:
1.http://www.naun.org/multimedia/NAUN/computers/20-462.pdf
2.http://blog.csdn.net/gzlaiyonghao/article/details/3166735
'''
from PIL import Image
import sys
def image_ifo(image):
    try:
        img = Image.open(image)
    except Exception,e:
        print "Can not open the image!"
    print 'Image Mode:%s,Image Size:%s,Image Format:%s' % (img.mode,img.size,img.format)
    return img
def preprocessed_image(image):
    img = image_ifo(image)
    if not img.mode == 'YCbCr':
        img = img.convert('YCbCr')
    return img
    
def detector(image):
    img = preprocessed_image(image)
    ycbcr_data = img.getdata()
    W,H = img.size
    THRESHOLD = 0.3
    count = 0
    for i,ycbcr in enumerate(ycbcr_data):
        y,cb,cr = ycbcr
        #if 80 <= cb <= 120 and 133 <= cr <= 173:
        if 86 <= cb <= 127 and 130 <= cr < 168:
            count += 1
    if count > THRESHOLD*W*H:
        print 'The image is pornographic!'
    else:
        print 'The image is not pornographic!'
        
if __name__ == '__main__':
    image = sys.argv[-1]
    print 'Detector is working on it,please wait a second...'
    detector(image)
    print 'Detecting is done!'
        
