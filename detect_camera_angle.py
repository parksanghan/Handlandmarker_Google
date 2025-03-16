import cv2
import mediapipe as mp
import numpy as np

# Mediapipe 초기화
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# 얼굴 Mesh 감지 모델 로드
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)

# 카메라 실행
cap = cv2.VideoCapture(0)

def get_camera_tilt(landmarks, image_w, image_h):
    # 왼쪽 눈(왼쪽 모서리)과 오른쪽 눈(오른쪽 모서리) 좌표 가져오기
    left_eye = np.array([landmarks[33].x * image_w, landmarks[33].y * image_h])
    right_eye = np.array([landmarks[263].x * image_w, landmarks[263].y * image_h])

    # 두 눈을 잇는 직선의 기울기 계산
    dx = right_eye[0] - left_eye[0]
    dy = right_eye[1] - left_eye[1]
    angle = np.degrees(np.arctan2(dy, dx))

    return angle

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # BGR → RGB 변환
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # 얼굴 랜드마크를 화면에 그림
            mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)

            # 얼굴 기울기 측정
            tilt_angle = get_camera_tilt(face_landmarks.landmark, frame.shape[1], frame.shape[0])

            # 화면에 각도 표시
            cv2.putText(frame, f"Camera Tilt: {tilt_angle:.2f} degrees", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # 30도 이상 기울어진 경우 경고 표시
            if abs(tilt_angle) >= 30:
                cv2.putText(frame, "Camera Tilted 30 degrees!", (50, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("MediaPipe Camera Tilt Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
