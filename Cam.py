import cv2
import sqlite3 as sq
cam = cv2.VideoCapture(0)

cv2.namedWindow("capture image")
db = sq.connect("database.db")
try:
    st = """
        CREATE TABLE num
        (id TEXT)
        """
    
    db.execute(st)
    insert = "INSERT INTO num(id) VALUES ('{}')".format(0)
    db.execute(insert)
    db.commit()

except:
    pass

fetc = """SELECT id FROM num"""
data = db.execute(fetc)
img_counter = 0
for row in data:
    img_counter = ''.join(row)
    
img_counter = int(img_counter)
    
while True:
    ret,frame = cam.read()

    if not ret:
        print('failed')
        break
    cv2.imshow('test',frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        print('closing')
        break
    elif k%256 == 32:
        img_name = "Training_images/picture{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print('captured')
        img_counter +=1
        insert = "UPDATE num SET id = "+ str(img_counter) 
        db.execute(insert)
        db.commit()


cam.release()
cam.destroyAllWindows()


    