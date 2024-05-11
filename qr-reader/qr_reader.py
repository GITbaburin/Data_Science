import cv2
from pyzbar.pyzbar import decode

def detect_and_decode_qr_codes(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    decoded_objects = decode(gray)
    
    if not decoded_objects:
        print("No QR codes found in the image.")
        return

    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        print(f"QR Code Data: {data}")
        
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            points = hull
        for j in range(4):
            cv2.line(image, tuple(points[j]), tuple(points[(j+1) % 4]), (0, 0, 255), 3)
    
    #cv2.imshow("QR Code Detection", image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

detect_and_decode_qr_codes("PATH_YO_YOUR_QR_CODE")
