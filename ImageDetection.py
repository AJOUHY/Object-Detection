import cv2
import numpy as np
def detectImage(filename):
    thres = 0.45 # Threshold to detect object
    img = cv2.imread(filename)


    classNames= []
    classFile = 'coco.names'
    with open(classFile,'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'

    net = cv2.dnn_DetectionModel(weightsPath,configPath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/ 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    #while True:
        #success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    print(classIds,bbox)

    COLORS = np.random.uniform(0, 255, size=(len(classNames), 3))
        #if len(classIds) != 0:
    for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
        # cv2.rectangle(img,box,color=(0,255,0),thickness=2)
        # cv2.putText(img,classNames[classId-1],(box[0],box[1]+30),
        #                 cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        # cv2.putText(img,str(round(confidence*100,2)),(box[0],box[1]-10),
        #                     cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


        (startX, startY, endX, endY) = box.astype("int")
        # display the prediction
        label = "{}: {:.2f}%".format(classNames[classId-1], confidence * 100)
        cv2.rectangle(img,box ,COLORS[classId-1], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(img, label, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[classId-1], 2)

    cv2.imwrite('ImgToSend/img0.jpg', img)
    #cv2.imshow("Output",img)
    #cv2.waitKey(0)