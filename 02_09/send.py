
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
import socket
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local_host = socket.gethostname()
udp_ip = socket.gethostbyname(local_host)   
print (udp_ip)
udp_port = 23456


centers = []
centers_send = []
colors = []
radii = []

show_video = False

video = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while(True):
        time.sleep(.15)
        ret, frame =  video.read()
        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame)
   
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if not results.multi_hand_landmarks:
            pass
        else:
            for hand_landmarks in results.multi_hand_landmarks:
                for landmark in hand_landmarks.landmark:
                    x = int(landmark.x*frame.shape[1])
                    y = int(landmark.y*frame.shape[0])
                    z = int(landmark.z*frame.shape[0])
                    radius = int(abs(z/2) + 1)
                    center = (x,y)
                    center_send = (x, y, z)
                    rgb_color = (255-x,255-y, 255+z)
                    centers.append(center)
                    centers_send.append(center_send)
                    colors.append(rgb_color)
                    radii.append(radius)
                    if len(centers) >= 22:
                            centers.pop(0)
                            centers_send.pop(0)
                            colors.pop(0)
                            radii.pop(0)
                    for i in range(len(centers)):
                        
                        cv2.circle(frame, centers[i], radii[i] , colors[i], 1)
                        msg = (str(centers_send)).encode("utf-8")
                        sock.sendto(msg, (udp_ip, udp_port))
                        


        if show_video:            
            cv2.imshow('MediaPipeHands', (cv2.flip(frame, 1)))
        
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
            
    
video.release()

cv2.destroyAllWindows()




