# opencv-old-black-and-white-camera

Video Recorder (영상 녹화기)

기본 설명

OpenCV를 사용하여 컴퓨터의 웹캠(또는 카메라)으로 실시간 영상을 표시하고, 녹화 기능을 제공하는 간단한 비디오 레코더.

주요 기능

1. 실시간 웹캠 영상 출력
2. 녹화 기능 (AVI 또는 MP4 형식으로 저장 가능)
3. Preview (대기) / Record (녹화) 모드 전환
4. Space 키를 눌러 녹화 시작/중지 (녹화 중일 때만 빨간 원 표시됨)
5. ESC 키를 눌러 프로그램 종료
6. G 키를 눌러 흑백 모드 ON/OFF 


실행 방법

1. OpenCV 설치 (Python 환경 필요)

pip install opencv-python opencv-contrib-python

2️. 프로그램 실행

Python 환경에서 아래 명령어를 실행합니다.

python video_recorder.py


사용 방법

1️. 프로그램을 실행하면 웹캠 화면이 표시
2. Space 키를 눌러 녹화 시작/중지 (녹화 중일 때만 빨간 원 표시)
3. 녹화 중일때만 빨간색 원이 화면에 표시
4️. G 키를 눌러 흑백 모드 ON/OFF
5. ESC 키를 누르면 프로그램이 종료

코드 설명

cv2.VideoCapture(0): 웹캠 영상 가져오기

cv2.VideoWriter(): 영상 녹화 및 저장

cv2.imshow(): 화면에 실시간 영상 표시

cv2.waitKey(): 키 입력 이벤트 처리 (Space, ESC, G)

cv2.circle(): 녹화 중일 때만 빨간 원 표시 및 녹화 반영

cv2.addWeighted(): 흑백 모드에서도 빨간 원 유지하기 위해 컬러 프레임과 합성


녹화된 영상 저장

 녹화된 파일은 기본적으로 output.avi로 저장됩니다.

1️. 파일 위치 확인

 Windows: 파일 탐색기에서 output.avi 검색

 Mac/Linux: 터미널에서 확인

 ls -l output.avi

2️. 녹화된 영상 재생

 Windows에서 실행

 output.avi를 더블 클릭하여 기본 플레이어로 열기

 VLC 플레이어 추천 (설치 필요)

2-1. Python 코드로 재생

 import cv2
 cap = cv2.VideoCapture("output.avi")
 while cap.isOpened():
     ret, frame = cap.read()
     if not ret:
         break
     cv2.imshow("Recorded Video", frame)
     if cv2.waitKey(25) & 0xFF == 27:  # ESC 키로 종료
         break
 cap.release()
 cv2.destroyAllWindows()


실행 화면 (예시 이미지 첨부)

![image](https://github.com/user-attachments/assets/0069b0ee-2f21-48d8-9e24-192066c04347)


