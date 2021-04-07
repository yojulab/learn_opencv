from cv2 import cv2 as cv
 
# Load a model imported from Tensorflow
# more refer : https://junha1125.github.io/artificial-intelligence/2020-08-15-2OpenCVcode/
# get inference weight file
#   wget http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet50_coco_2018_01_28.tar.gz
#   tar -xvzf ./faster_rcnn_resnet50_coco_2018_01_28.tar.gz
#   
# get config file
#   wget https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/faster_rcnn_resnet50_coco_2018_01_28.pbtxt
#
# wget -O beach.png https://www.tensorflow.org/hub/tutorials/tf2_object_detection_files/output_hX-AWUQ1wIEr_0.png
pb_file = 'App/DNN/faster_rcnn_resnet50_coco_2018_01_28/frozen_inference_graph.pb'
cfg_file = 'App/DNN/faster_rcnn_resnet50_coco_2018_01_28.pbtxt'

labels_to_names = {0:'person',1:'bicycle',2:'car',3:'motorcycle',4:'airplane',5:'bus',6:'train',7:'truck',8:'boat',9:'traffic light',
                    10:'fire hydrant',11:'street sign',12:'stop sign',13:'parking meter',14:'bench',15:'bird',16:'cat',17:'dog',18:'horse',19:'sheep',
                    20:'cow',21:'elephant',22:'bear',23:'zebra',24:'giraffe',25:'hat',26:'backpack',27:'umbrella',28:'shoe',29:'eye glasses',
                    30:'handbag',31:'tie',32:'suitcase',33:'frisbee',34:'skis',35:'snowboard',36:'sports ball',37:'kite',38:'baseball bat',39:'baseball glove',
                    40:'skateboard',41:'surfboard',42:'tennis racket',43:'bottle',44:'plate',45:'wine glass',46:'cup',47:'fork',48:'knife',49:'spoon',
                    50:'bowl',51:'banana',52:'apple',53:'sandwich',54:'orange',55:'broccoli',56:'carrot',57:'hot dog',58:'pizza',59:'donut',
                    60:'cake',61:'chair',62:'couch',63:'potted plant',64:'bed',65:'mirror',66:'dining table',67:'window',68:'desk',69:'toilet',
                    70:'door',71:'tv',72:'laptop',73:'mouse',74:'remote',75:'keyboard',76:'cell phone',77:'microwave',78:'oven',79:'toaster',
                    80:'sink',81:'refrigerator',82:'blender',83:'book',84:'clock',85:'vase',86:'scissors',87:'teddy bear',88:'hair drier',89:'toothbrush',
                    90:'hair brush'}

tensorflowNet = cv.dnn.readNetFromTensorflow(pb_file, cfg_file)
 
for t in tensorflowNet.getLayerTypes():
    print('\t%d layers of type %s' % (tensorflowNet.getLayersCount(t), t))

# Input image
image_path = 'datas/images/beach.png'
# image_path = 'datas/images/raccoon-1.jpg'
draw_img = cv.imread(image_path)
rows, cols, channels = draw_img.shape
 
import time
start = time.time()
# Use the given image as input, which needs to be blob(s).
tensorflowNet.setInput(cv.dnn.blobFromImage(draw_img, swapRB=True, crop=False))  # add size=(300, 300), 
 
# Runs a forward pass to compute the net output
networkOutput = tensorflowNet.forward()
 
# Loop on the outputs
for detection in networkOutput[0,0]:
    
    score = float(detection[2])
    class_id = int(detection[1])
    if score > 0.2:
    	
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
 
        caption = "{}: {:.4f}".format(labels_to_names[class_id], score)
        print(caption)
        #draw a red rectangle around detected objects
        cv.rectangle(draw_img, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)
        cv.putText(draw_img, caption, (int(left), int(top - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
 
print('Detection During Time :',round(time.time() - start, 2),"second")
# Show the image with a rectagle surrounding the detected objects 
cv.imshow('Image', draw_img)
cv.waitKey()
cv.destroyAllWindows()