import cv2
import numpy as np

final_output = np.fromfile('text -1.dat',dtype = float)
print(final_output)
cap = cv2.VideoCapture("Burglary021_x264.mp4")
ret,frame = cap.read()
writer = cv2.VideoWriter('anomaly-output-1.mp4', cv2.VideoWriter_fourcc(*'MP4V'), cap.get(cv2.CAP_PROP_FPS),(frame.shape[1], frame.shape[0]))
for i in range(1,len(final_output)-1):
    ret,frame = cap.read()
    frame = cv2.putText(frame,str(final_output[i]),(10,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,0),1)
    cv2.imshow('frames',frame)
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q') & ret:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()