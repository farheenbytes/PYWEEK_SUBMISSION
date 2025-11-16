import cv2

# ---------- 1. Load Image ----------
img = cv2.imread("image.png")
if img is None:
    raise SystemExit("Image not found!")

h, w = img.shape[:2]

# ---------- SHOW ORIGINAL EXACTLY AS IT IS ----------
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original", w, h)
cv2.imshow("Original", img)

# ---------- 2. Resize to 1/4 ----------
resized = cv2.resize(img, (w // 4, h // 4), interpolation=cv2.INTER_AREA)

# ---------- 3. Color Conversions ----------
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
lab  = cv2.cvtColor(resized, cv2.COLOR_BGR2LAB)

# ---------- 4. Gaussian Blur ----------
blur = cv2.GaussianBlur(resized, (15, 15), 0)

# ---------- 5. Show Everything ----------
cv2.imshow("Resized 1/4", resized)
cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("LAB", lab)
cv2.imshow("Blurred", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
