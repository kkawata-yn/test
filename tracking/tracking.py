# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():

	cap = cv2.VideoCapture("sample10.mp4")

	#フレームレートを取得
	frame_rate = int(cap.get(5))

	#フレームの幅を取得
	frame_width = int(cap.get(3))

	#フレームの高さを取得
	frame_height = int(cap.get(4))


	#VideoWriterを作成(処理した動画を書き込む)
	#fourccは、FourCCを表す4つのリスト(mp4で保存することを示す)
	fourcc = cv2.VideoWriter_fourcc("M","P","4","V")
	writer = cv2.VideoWriter("opt_flow6.mp4" ,fourcc, frame_rate, (frame_width / 4, frame_height / 4),3)  #trueはカラー画像、falseはグレーを保存

	i = 0

	while(cap.isOpened()):
	
		ret, frame = cap.read()

		if(i == 0):
			frame1 = frame
			height, width = frame1.shape[:2]

			frame1 = cv2.resize(frame1, (width/4, height / 4))

			i = 1
		else:
			if (ret):
				frame2 = frame

				frame2 = cv2.resize(frame2, (width/4, height / 4))

				gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

				gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

				flow = cv2.calcOpticalFlowFarneback(gray1, gray2, None ,0.5, 3, 15, 3, 5, 1.2, 0)

				kari = frame1			
			
				visual_flow = visualizeFarnebackFlow(kari, flow, height, width)

				writer.write(visual_flow)

				frame1 = frame2

				cv2.imshow("flow", visual_flow)
				if cv2.waitKey(1) & 0xFF == ord("q"):
					break

			else: 
				break

	cap.release()
	writer.release()
	cv2.destroyAllWindows()

def visualizeFarnebackFlow(orgimg, flow, height, width):

	for i in range(0 , height / 4, 10):
		for j in range(0, width / 4, 10):
			fx = flow[i,j,0]  #x成分のベクトルの大きさ
			fy = flow[i,j,1]  #y成分のベクトルの大きさ

			print(str(i) + "行" + str(j) + "列 fx: " + str(fx))
			print(str(i) + "行" + str(j) + "列 fy: " + str(fy))

			if (fx > 1) | (fy > 1):
				if i + fx >= i :
					orgimg = cv2.line(orgimg,(j,i),(int(j + fy),int(i + fx)),(255,0,0),1)

				else:	
					orgimg = cv2.line(orgimg,(int(j + fy),int(i + fx)),(j,i),(0,0,255),1)
							
	return orgimg

main()