import cv2,time,numpy

video = cv2.VideoCapture(0)

ret_val,image = video.read()

cv2.imwrite(str(time.localtime().tm_year)+','+str(time.localtime().tm_hour)+','+str(time.localtime().tm_min)+','+str(time.localtime().tm_sec)+'.png',image)

video.release()

track = {'hour':time.localtime().tm_hour,'minute':time.localtime().tm_min,'seconds':time.localtime().tm_sec,'year':time.localtime().tm_year,'month':time.localtime().tm_mon,'date':time.localtime().tm_mday}

fopen = open('logs.txt','a')

fopen.write('\n'+str(track))

fopen.close()
