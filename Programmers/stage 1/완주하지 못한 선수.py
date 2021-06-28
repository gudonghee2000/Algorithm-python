import cv2
import numpy as np


def nothing(x):
    pass


def setTrackBar():
    cv2.namedWindow('20172703_공병주')

    # 창에 TrackBar를 추가해줍니다.
    cv2.createTrackbar('LowerH', '20172703_공병주', 0, 255, nothing)
    cv2.setTrackbarPos('LowerH', '20172703_공병주', 0)  # 범위의 H 최소값
    cv2.createTrackbar('UpperH', '20172703_공병주', 0, 255, nothing)
    cv2.setTrackbarPos('UpperH', '20172703_공병주', 25)  # 범위의 H 최댓값

    cv2.createTrackbar('LowerS', '20172703_공병주', 0, 255, nothing)
    cv2.setTrackbarPos('LowerS', '20172703_공병주', 69)  # 범위의 S 최소값
    cv2.createTrackbar('UpperS', '20172703_공병주', 0, 255, nothing)
    cv2.setTrackbarPos('UpperS', '20172703_공병주', 255)  # 범위의 S 최댓값

    cv2.createTrackbar('LowerI', '20172703_공병주', 0, 255, nothing)
    cv2.setTrackbarPos('LowerI', '20172703_공병주', 75)  # 범위의 I 최소값
    cv2.createTrackbar('UpperI', '20172703_공병주', 0, 255, nothing)
    cv2.setTrackbarPos('UpperI', '20172703_공병주', 255)  # 범위의 I 최댓값

    # 범위는 본인의 얼굴색에 맞게 조정해둠


setTrackBar()


def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant) - 1]


















