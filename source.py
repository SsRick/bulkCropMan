#for manually cropping a bilk of images
import numpy
import cv2
import os

refPt=[]
cropping=False
def crop(event,x,y,flag,param):
	global refPt,cropping 
	if event==cv2.EVENT_LBUTTONDOWN:
		refPt=[(x,y)]
		cropping=True
	elif event==cv2.EVENT_LBUTTONUP:
		refPt.append((x,y))
		cropping=False
		cv2.rectangle(image,refPt[0],refPt[1],(0,255,253),1)
		cv2.imshow('image',image)


cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image',crop)
with open('toCrop.txt') as f:
	content=f.readlines()

content=[x.strip() for x in content]

i=0
for im in content:
        refPt[:]=[]
	image=cv2.imread(im)
	height,width=image.shape[:2]
	scale=float(720)/height
	image=cv2.resize(image,None,fx=scale,fy=scale,interpolation=cv2.INTER_AREA)
	cpy=image.copy()
	while True:
		cv2.imshow('image',image)
		key=cv2.waitKey(1) & 0xFF
		if key==ord("n"):
			break
		elif key==ord("q"):
			exit()
		elif key==ord("s"):
			if len(refPt)==2:
				roi=cpy[refPt[0][1]+2:refPt[1][1]+2,refPt[0][0]-1:refPt[1][0]-1]
				cv2.imshow('roi',roi)
				cv2.imwrite(os.path.join('cropped','sam'+str(i)+'.jpg'),roi)
				i=i+1
			elif key==ord("c"):
                                cv2.imshow('image',cpy)
                                refPt[:]=[]
				continue


cv2.waitKey(0)
cv2.destroyAllWindows()
