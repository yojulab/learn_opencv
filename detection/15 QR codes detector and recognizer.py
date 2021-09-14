# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
import cv2
import numpy as np


def intersect(l1, l2):
    delta = np.array([l1[1] - l1[0], l2[1] - l2[0]]).astype(np.float32)
    
    delta = 1 / delta
    delta[:, 0] *= -1
    
    b = np.matmul(delta, np.array([l1[0], l2[0]]).transpose())
    b = np.diagonal(b).astype(np.float32)
        
    res = cv2.solve(delta, b)
    return res[0], tuple(res[1].astype(np.int32).reshape((2)))


def rectify(image, corners, out_size):
    rect = np.zeros((4, 2), dtype = "float32")
    rect[0] = corners[0]
    rect[1] = corners[1]
    rect[2] = corners[2]
    rect[3] = corners[3]

    dst = np.array([
        [0, 0],
        [out_size[1] - 1, 0],
        [out_size[1] - 1, out_size[0] - 1],
        [0, out_size[0] - 1]], dtype = "float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    rectified = cv2.warpPerspective(image, M, out_size)
    return rectified


def qr_code_outer_corners(image):
    outer_corners_found = False
    outer_corners = []
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # cv2.imshow('image',image)
    # cv2.imshow('gray',gray)
    cv2.imshow('th',th)
    cv2.waitKey()

    # 찾을 물체는 흰색이어야하고 배경은 검은색 
    contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # ret = max(contours, key=len)
    # draw_contour = cv2.drawContours(gray, contours, -1, (0,255,0), 2)
    # draw_contour = cv2.drawContours(gray, [ret], 0, (0,255,0),2)
    for contour in contours:
        draw_contour = cv2.drawContours(gray, [contour], 0, (255,0,0), 2)
        cv2.imshow('draw_contour', draw_contour)
        cv2.waitKey()
    cv2.destroyAllWindows()
    
    cnts = []
    centers = []
    corners_point = list()
        
    hierarchy = hierarchy.reshape((-1, 4))
    for i in range(hierarchy.shape[0]):
        i_next, i_prev, i_child, i_par = hierarchy[i]
        if all(v == -1 for v in hierarchy[i][:3]) & all(v == -1 for v in hierarchy[i_par][:2]):
            ids = [i, i_par, hierarchy[i_par][3]]
            corner_cnts = []
            for id_ in ids:
                cnt = contours[id_]
                apprx = cv2.approxPolyDP(cnt, cv2.arcLength(cnt, True) * 0.02, True)
                if len(apprx) == 4:
                    corner_cnts.append(apprx.reshape((4, -1)))
            if len(corner_cnts) == 3:
                cnts.append(corner_cnts)
                all_pts = np.array(corner_cnts).reshape(-1, 2)
                centers.append(np.mean(all_pts, 0))
    
    # to deside top-right, top-left, bottom-left point
    if len(centers) == 3:
        centers_norm = [np.linalg.norm(center) for center in centers]
        top_right_index = np.argmax(centers_norm)

        distances_between_pts = np.linalg.norm(np.roll(centers, shift=1, axis=0) - centers, axis=1)
        max_dist_id = np.argmax(distances_between_pts)
        
        index_diag_pt_1 = max_dist_id       # top-right index
        index_diag_pt_2 = (max_dist_id - 1) % len(centers)  # bottom-left index
        index_corner_pt = (len(centers) - 1)*len(centers) // 2 - index_diag_pt_1 - index_diag_pt_2  # top
        # index_corner_pt = [item for item in range(3) if item not in [index_diag_pt_1, index_diag_pt_2]][0]

        middle_pt = 0.5 * (centers[index_diag_pt_1] + centers[index_diag_pt_2])
        
        i_ul_pt = np.argmax(np.linalg.norm(cnts[index_corner_pt][-1] - middle_pt, axis=1))
        ul_pt = cnts[index_corner_pt][-1][i_ul_pt]
                
        for i in [index_diag_pt_1, index_diag_pt_2]:
            corner_cnts = cnts[i]
            outer_cnt = corner_cnts[-1]     # outer line points
            
            distances_to_mp = np.linalg.norm(outer_cnt - middle_pt, axis=1)
            max_dist_id = np.argmax(distances_to_mp)      
        
            vec_from_mid_to_diag = outer_cnt[max_dist_id] - middle_pt
            vec_from_mid_to_corner = ul_pt - middle_pt
            cross_prod = np.cross(vec_from_mid_to_corner, vec_from_mid_to_diag)
        
            diff_idx = 0
        
            if cross_prod > 0:
                ur_pt = outer_cnt[max_dist_id]
                ur_pt_2 = outer_cnt[(max_dist_id + 1) % len(outer_cnt)]
            else:
                bl_pt = outer_cnt[max_dist_id]
                bl_pt_2 = outer_cnt[(max_dist_id - 1) % len(outer_cnt)]
                    
        ret, br_pt = intersect((bl_pt, bl_pt_2), (ur_pt, ur_pt_2))
        
        if ret == True:
            outer_corners_found = True
            outer_corners = [ul_pt, ur_pt, br_pt, bl_pt]
    
    return outer_corners_found, outer_corners

# read image
# frame = cv2.imread('./datas/images/qr_01.png') # can detect marker
frame = cv2.imread('./datas/images/qr_02.png') # can't detect marker
if frame is not None:
    # frame = cv2.flip(frame, 1)
    # cv2.imshow('flip', frame)
    result, corners = qr_code_outer_corners(frame)

    qr_code_size = 300

    if result:
        if all((0, 0) < tuple(c) < (frame.shape[1], frame.shape[0]) for c in corners):
            rectified = rectify(frame, corners, (qr_code_size, qr_code_size))
            
            cv2.circle(frame, tuple(corners[0]), 15, (0, 255, 0), 2)
            cv2.circle(frame, tuple(corners[1]), 15, (0, 0, 255), 2)
            cv2.circle(frame, tuple(corners[2]), 15, (255, 0, 0), 2)
            cv2.circle(frame, tuple(corners[3]), 15, (255, 255, 0), 2)
            
            frame[0:qr_code_size, 0:qr_code_size] = rectified

    window_name = "QR code detection"
    cv2.namedWindow(window_name, 0)
    cv2.resizeWindow(window_name, int(frame.shape[1]/3),int(frame.shape[0]/3))
    cv2.imshow(window_name, frame)

    cv2.waitKey()

# read video
# cap = cv2.VideoCapture('../datas/videos/qr.mp4')

# while cap.grab():
#     ret, frame = cap.read()
#     if ret == False:
#         break
    
#     result, corners = qr_code_outer_corners(frame)
    
#     qr_code_size = 300
    
#     if result:
#         if all((0, 0) < tuple(c) < (frame.shape[1], frame.shape[0]) for c in corners):
#             rectified = rectify(frame, corners, (qr_code_size, qr_code_size))
            
#             cv2.circle(frame, tuple(corners[0]), 15, (0, 255, 0), 2)
#             cv2.circle(frame, tuple(corners[1]), 15, (0, 0, 255), 2)
#             cv2.circle(frame, tuple(corners[2]), 15, (255, 0, 0), 2)
#             cv2.circle(frame, tuple(corners[3]), 15, (255, 255, 0), 2)
            
#             frame[0:qr_code_size, 0:qr_code_size] = rectified

#     cv2.imshow('QR code detection', frame)
    
#     k = cv2.waitKey(100)
    
#     if k == 27:
#         break

# cap.release()
cv2.destroyAllWindows()





