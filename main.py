import cv2

video = cv2.VideoCapture("Aa Zra.mp4")
success, frame = video.read()

count = 1
while success:
  cv2.imwrite(f'images/{count}.jpg', frame)
  success, frame = video.read()
  count += 1