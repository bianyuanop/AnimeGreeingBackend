import base64
import pymongo
from termcolor import colored

DB_CONF = {
    'name': 'iamges'
}

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

def createDBConn(db, addr="mongodb://localhost:27017/"):
    client = pymongo.MongoClient(addr)
    return client[db]


def retriveDataURI(_id, mongo_col):
    res = []
    query = mongo_col.find({'_id': _id})
    for x in query:
        res.append(x['uri'])
    return res

def insertDataURI(uri, mongo_col):
    x = mongo_col.insert_one({'uri': uri})
    return x.inserted_id

def insertMultipleDataURI(uris, mongo_col):
    x = mongo_col.insert_many(uris)
    return x.inserted_ids
    

if __name__ == '__main__':
    mydb = createDBConn('animePrj')
    mycol = mydb['images']
    
    _id = insertDataURI('test', mycol)
    datauri = retriveDataURI(_id, mycol)
    print(datauri)
