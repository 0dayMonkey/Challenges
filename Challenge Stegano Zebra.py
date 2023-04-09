import cv2
import pyzbar.pyzbar as pyzbar


def read_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def find_qrs(gray_image):
    return pyzbar.decode(gray_image)


def draw_qrs(image, qrs):
    for qr in qrs:
        (x, y, w, h) = qr.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        qrData = qr.data.decode("utf-8")
        qrType = qr.type
        text = "{} ({})".format(qrData, qrType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    return image


def main():
    image_path = r"../../Documents/GitHub/Challenges/zebr.png"
    gray_image = read_image(image_path)
    qrs = find_qrs(gray_image)
    print(qrs)

    image_with_qrs = draw_qrs(cv2.imread(image_path), qrs)

    cv2.imshow("Image", image_with_qrs)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
