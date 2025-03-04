import cv2

# 1. Wczytaj i wyświetl obraz z podanej przez siebie ścieżki
image = cv2.imread("bytom.jpg")
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

# Sprawdź, co się stanie, gdy podasz błędną ścieżkę.
imageInvalid = cv2.imread("warszawa.jpg")
if imageInvalid is None:
    print("Plik z błędną lokalizacją nie wczytuje się!")

# 2. Wczytaj zdjęcie w kolorze i wyświetl liczbę kanałów
(h, w, c) = image.shape
print('Bytom w pełnej okazałości:')
print(f'- width: {w} pixels')
print(f'- height: {h} pixels')
print(f'- channels: {c}')

# 3. Wczytaj zdjęcie w odcieniach szarości i wyświetl liczbę kanałów
image_gray = cv2.imread("bytom.jpg", cv2.IMREAD_GRAYSCALE)
(h_gray, w_gray) = image_gray.shape
print('Bytom w odcieniach szarości:')
print(f'- width: {w_gray} pixels')
print(f'- height: {h_gray} pixels')
print(f'- channels: 1')

# 4. Wczytaj obraz w skali szarości i zapisz go jako nowy plik
cv2.imwrite("bytom_gray.jpg", image_gray)
print("Obraz zapisano jako bytom_gray.jpg")

# 5. Otwórz dwa obrazy jednocześnie w osobnych oknach
cv2.imshow("Obraz kolorowy", image)
cv2.imshow("Obraz szary", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Dostosowanie do ekranów
cv2.namedWindow("Obraz dostosowany do ekranu", cv2.WINDOW_NORMAL)
cv2.imshow("Obraz dostosowany do ekranu", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
