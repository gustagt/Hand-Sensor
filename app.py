import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from cvzone.HandTrackingModule import HandDetector
from utils.validations import valFingers, valHandPosition, valThumbFinger

retorno = None

# fução callback do gesture
def callback_gesture(result: vision.GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):  # type: ignore
    global retorno
    retorno = result

# configuração base do gesture
options = vision.GestureRecognizerOptions(
    num_hands=1,
    base_options=python.BaseOptions(model_asset_path='models/gesture_recognizer.task'),
    running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
    result_callback=callback_gesture,
)

# instancia o reconhecimento de gestos
with vision.GestureRecognizer.create_from_options(options) as recognizer:

    # instancia da captura de video e modelos para landmarks e o box da mao.
    cap = cv2.VideoCapture(0)  
    hands = mp.solutions.hands  
    handDetector = hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
    detector = HandDetector(detectionCon=0.8, maxHands=1)
    mpDwaw = mp.solutions.drawing_utils

    # Loop de captura
    while True:
        
        success, frame = cap.read()
        if not success:
            print("Erro ao capturar frame.")
            break
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # conversão da imagem para ser usado na função recognize_async 
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        recognizer.recognize_async(mp_image, timestamp_ms=int(cap.get(cv2.CAP_PROP_POS_MSEC)))

        # instancia das variaveis para a logica 
        coordinates = []
        contador = 0

        # busca de dados 
        height, width, _ = frame.shape
        results_handDetector = handDetector.process(frame_rgb)
        handPoints = results_handDetector.multi_hand_landmarks
        handleBox = detector.findHands(frame,draw=False,flipType=False)

        # logica quando a mão for detectada
        if handPoints and retorno and retorno.gestures:
            
            # busca o gesto indentificado pelo detector
            gesture_name = retorno.gestures[0][0].category_name
            # Define se é a mão esquerda ou direita
            handedness = 'right' if results_handDetector.multi_handedness[0].classification[0].index == 0 else 'left'
            
        
            for points in handPoints:
                # desenho das conexões da mão
                mpDwaw.draw_landmarks(frame, points,hands.HAND_CONNECTIONS)

                # montagem do arrai de coordenadas
                for id, cord in enumerate(points.landmark):
                    coordinateX, coordinateY = int(cord.x * width), int(cord.y * height)

                    coordinates.append((coordinateX,coordinateY))
                

                dedos = [8,12,16,20]
                
                # logica para a contagem de dedos
                if coordinates:
                    handPosition = valHandPosition(coordinates)         
                    if valThumbFinger(coordinates,handPosition): contador+=1
                    for index in dedos:
                        if valFingers(coordinates, index,handPosition): contador+=1

            # Escreve o gesto na tela.
            cv2.putText(
                frame,
                f'Gesture: {gesture_name} ',
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0), 
                2
            )

            # desenha a caixa e escreve o texto na identificação da mão
            if handleBox[0]:
                boxX, boxY, boxW, boxH = handleBox[0][0]['bbox']
                # caixa ao redor da mão
                cv2.rectangle(frame, (boxX-20, boxY-20), (boxX+boxW+20,boxY+boxH+20), (0, 0, 0), 3)
                # fundo para o texto em cima da caixa
                cv2.rectangle(frame, (boxX-20, boxY-50), (boxX+150,boxY-20), (0, 0, 0), -1)
                # texto sobre a caixa
                cv2.putText(frame,str(contador)+" "+handedness,(boxX+5,boxY-25),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)


       
        cv2.imshow('Frame', frame)

      
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
