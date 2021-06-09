import base64
import pymongo
from termcolor import colored

client = pymongo.MongoClient("mongodb://localhost:27017/")

def imageEntity2dataUri(imgBuf, imgType):
    
    prefix = 'data:image/' + imgType + ';' + 'base64,'
    dataStr = base64.b64encode(imgBuf)

    return prefix + dataStr.decode('utf8')

def dataUri2ImgEntity(uri):

    uriArr = uri.split(',')
    prefix = uriArr[0]
    data = uriArr[1]

    imgInfo = prefix.split(';')
    encodingMethod = imgInfo[1]
    imageType = imgInfo[0].split('/')[1]

    if encodingMethod == 'base64':
        plainData = base64.b64decode(data)

        with open("/tmp/tempImage." + imageType, 'wb') as f:
            f.write(plainData)
            print(colored('[INFO]', 'green'), "image decoded wrote to /tmp")

def retriveDataURI():
    pass

def insertDataURI(uri):
    pass
    

if __name__ == '__main__':
    origin = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=='
    dataUri2ImgEntity(origin)

    with open('/tmp/tempImage.png', 'rb') as f:
        buf = f.read()

    dataURI = imageEntity2dataUri(buf, 'png')

    print(origin)
    print(dataURI)
    print(origin == dataURI)
