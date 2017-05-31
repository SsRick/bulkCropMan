import numpy
import cv2

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
		cv2.rectangle(image,refPt[0],refPt[1],(0,255,253),2)
		cv2.imshow('image',image)


cv2.namedWindow('image')
cv2.setMouseCallback('image',crop)
with open('he.txt') as f:
	content=f.readlines()

i=0
for im in content:
	image=cv2.imread(im)
	while True:
		cv2.imshow('image',image)
		key=cv2.waitKey(1) & 0xFF
		if key==ord("n"):
			break
		elif key==ord("q"):
			exit()
		elif key==ord("s"):
			if len(refPt)==2:
				roi=image[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]]
				cv2.imshow('roi',roi)
				cv2.imwrite('sam'+str(i),roi)
				i=i+1
			elif key==ord("c"):
				continue


cv2.waitKey(0)
cv2.destroyAllWindows()
