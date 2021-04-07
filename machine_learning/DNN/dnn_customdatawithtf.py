# https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/auto_examples/plot_object_detection_saved_model.html

from cv2 import cv2 as cv 
import tensorflow as tf

PATH_TO_SAVED_MODEL = 'App/DNN/saved_model' 
detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)

image_path = 'datas/images/raccoon-1.jpg'  
labels_to_names = {0:'raccoon', 1:'raccoon'}, 
# image_path = 'datas/images/beach.png'   
print('Running inference for {}... '.format(image_path), end='')

draw_img = cv.imread(image_path)
rows, cols, channels = draw_img.shape

input_tensor = tf.convert_to_tensor(draw_img)      # [417, 650, 3]
input_tensor = input_tensor[tf.newaxis, ...]        # [1, 417, 650, 3]

import time
start = time.time()
networkOutput = detect_fn(input_tensor)                # networkOutput.keys()

scores = networkOutput['detection_scores'][0]
boxes = networkOutput['detection_boxes'][0]
class_ids = networkOutput['detection_classes'][0]
for class_id, score, box in zip(class_ids, scores, boxes):
    if score > 0.01:
        left = box[0] * cols
        top = box[1] * rows
        right = box[2] * cols
        bottom = box[3] * rows
 
        # caption = "{}: {:.4f}".format(labels_to_names[class_id], score)
        # print(caption)
        #draw a red rectangle around detected objects
        cv.rectangle(draw_img, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)
        # cv.putText(draw_img, caption, (int(left), int(top - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
 
print('Detection During Time :',round(time.time() - start, 2),"second")
# Show the image with a rectagle surrounding the detected objects 
cv.imshow('Image', draw_img)
cv.waitKey()

# from object_detection.utils import label_map_util
# from object_detection.utils import visualization_utils as viz_utils
# viz_utils.visualize_boxes_and_labels_on_image_array(
#         image_np_with_detections,
#         detections['detection_boxes'],
#         detections['detection_classes'],
#         detections['detection_scores'],
#         None,   #category_index,
#         use_normalized_coordinates=True,
#         max_boxes_to_draw=200,
#         min_score_thresh=.30,
#         agnostic_mode=False)

# # for boxes, scores in detections['detection_boxes'], detections['detection_scores']:
# #     print(boxes, scores)
# for scores in detections['detection_scores']:
#     print(scores)

# cv.imshow('Image', image_np_with_detections)
# cv.waitKey()