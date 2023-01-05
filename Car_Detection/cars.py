import cv2

cars_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'cars_cascade.xml')

video_src = "Traffic.mp4"

cap = cv2.VideoCapture(video_src)

while True:
    ret, video = cap.read()
    
    if not ret:
        print("Video Okunamadı")
        
    else: 
        gray_video = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        cars = cars_cascade.detectMultiScale(gray_video,1.1,2)
        
        for(x, y, w, h) in cars:
            cv2.rectangle(video,(x,y),(x+w,y+h),(255,0,255),2)
            cv2.imshow("Cars Detection", video)
            if cv2.waitKey(50) & 0xFF== ord('q'):
                break
            
cv2.destroyAllWindows()

        
        