import cv2
import numpy as np


def sift_features(img):
	feature = cv2.xfeatures2d.SIFT_create()
	feature_pts, descriptors = feature.detectAndCompute(img, None)
	scores = 0
	# feature_pts = np.array([x.pt for x in feature_pts], dtype=np.float32)
	return {
		'keypoints': feature_pts,
		'descriptors': descriptors,
	}


def orb_features(img):
	feature = cv2.ORB_create(nfeatures=1500)
	feature_pts, descriptors = feature.detectAndCompute(img, None)
	scores = 0
	# feature_pts = np.array([x.pt for x in feature_pts], dtype=np.float32)
	return {
		'keypoints': feature_pts,
		'descriptors': descriptors,
	}


def surf_features(img):
	feature = cv2.xfeatures2d.SURF_create()
	feature_pts, descriptors = feature.detectAndCompute(img, None)
	scores = 0
	# feature_pts = np.array([x.pt for x in feature_pts], dtype=np.float32)
	return {
		'keypoints': feature_pts,
		'descriptors': descriptors,
	}


def good_features(img):
	pass


def fast_feature(img):
	feature = cv2.FastFeatureDetector_create(threshold=25, nonmaxSuppression=True)
	feature_pts, descriptors = feature.detectAndCompute(img, None)
	scores = 0
	# feature_pts = np.array([x.pt for x in feature_pts], dtype=np.float32)
	return {
		'keypoints': feature_pts,
		'descriptors': descriptors,
	}