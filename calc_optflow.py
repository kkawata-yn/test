# -*- coding: utf-8 -*-
import cv2
import numpy as np
from glob import glob

def main():

	#基準画像読み込み
	orgimg = cv2.imread("photo1.PNG")
	gray1 = cv2.cvtColor(orgimg, cv2.COLOR_BGR2GRAY)
	height, width = orgimg.shape[:2]
	newimg = np.zeros_like(orgimg)
	cv2.imwrite("photo1.jpg", orgimg)
	
	#画像読み込み
	for fn in glob("*.png"):
	 	cimg = cv2.imread(fn)
		print(cimg[0,0])
		newimg[0,0] = cimg[0,0]
		print(newimg[0,0])
		gray2 = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY)
		
		#opticalflowする
		flow = cv2.calcOpticalFlowFarneback(gray1, gray2, None ,0.5, 3, 15, 3, 5, 1.2, 0)


		#opticalして推定できたベクトルから、ズレを直して局所位置合わせを行う
		for i in range(height):
			for j in range(width):
				fx = flow[i,j,0]
				print(fx)
				fy = flow[i,j,1]
				print(fy)

				if (i + fy > height) | (j + fx > width) :
					fx = 0
					fy = 0

				if (i + fy < 0) | (j + fx < 0) :
					fx = 0
					fy = 0

				ii = i + fy
				jj = j + fx

				newimg[0,0] = cimg[0,0]
				print(newimg[0,0])


				newimg[i,j] = cimg[int(ii),int(jj)]
				print(newimg[i,j])
		cv2.imwrite(fn + "_opt.jpg", newimg)

			
main()