import cv2
import numpy as np

# 웹캠 열기
cap = cv2.VideoCapture(0)  # 0번 카메라 사용
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

# 녹화 설정 (저장할 파일, 코덱, FPS, 해상도)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정 (AVI 포맷)
fps = 20.0
frame_size = (int(cap.get(3)), int(cap.get(4)))  # (width, height)
out = cv2.VideoWriter('output.avi', fourcc, fps, frame_size, isColor=True)

recording = False  # 초기 상태: 녹화 안 함
gray_mode = False  # 초기 상태: 컬러 모드

while True:
    ret, frame = cap.read()  # 프레임 읽기
    if not ret:
        break

    # 원본 컬러 프레임 복사
    processed_frame = frame.copy()

    # 🎥 녹화 중일 때만 빨간 원 추가 🎥
    if recording:
        cv2.circle(processed_frame, (50, 50), 10, (0, 0, 255), -1)

    # 흑백 모드일 경우 변환 (빨간 원을 유지하면서 흑백 적용)
    if gray_mode:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 흑백 변환
        processed_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)  # 다시 3채널 변환
        if recording:
            cv2.circle(processed_frame, (50, 50), 10, (0, 0, 255), -1)  # 흑백에서도 빨간 원 유지

    # 🎥 녹화 중이면 현재 프레임을 파일에 저장
    if recording:
        out.write(processed_frame)

    cv2.imshow('Video Recorder', processed_frame)  # 화면에 표시

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 키: 종료
        break
    elif key == 32:  # Space 키: 녹화 시작/중지 토글
        recording = not recording
        print("녹화 중" if recording else "대기 모드")
    elif key == ord('g'):  # 'G' 키: 흑백 모드 토글
        gray_mode = not gray_mode
        print("흑백 모드 ON" if gray_mode else "컬러 모드")

# 종료 처리
cap.release()
out.release()
cv2.destroyAllWindows()
