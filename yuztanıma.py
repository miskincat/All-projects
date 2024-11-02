import cv2
import face_recognition
import os

# Resim yolunu dinamik olarak ayarla
image_path = os.path.expanduser("~/Masaüstü/projeler/hakkı.jpg")

# Kendi yüz resmini yükle ve yüz kodlarını tanımla
known_image = face_recognition.load_image_file(image_path)
known_encoding = face_recognition.face_encodings(known_image)[0]

# Kamerayı aç
video_capture = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare yakala
    ret, frame = video_capture.read()

    # Kareyi küçült (işlem hızını artırmak için)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Karedeki yüzleri bul ve kodla
    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    for face_encoding in face_encodings:
        # Tanınan yüz ile karşılaştır
        match = face_recognition.compare_faces([known_encoding], face_encoding)

        # Eşleşme bulunduysa, Hoş geldin yazısı göster
        if match[0]:
            cv2.putText(frame, "Hos geldin, Hakki", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Sonucu ekranda göster
    cv2.imshow('Video', frame)

    # 'q' tuşuna basarak çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera ve pencereleri serbest bırak
video_capture.release()
cv2.destroyAllWindows()