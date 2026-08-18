import cv2

# Cargar la imagen original
imagen = cv2.imread("edificio.jpg")

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar los bordes de la imagen
bordes = cv2.Canny(gris, 100, 200)

# Guardar la imagen resultante
cv2.imwrite("bordes_edificio.jpg", bordes)

# Mostrar la imagen con los bordes
cv2.imshow("Bordes del edificio", bordes)

# Esperar hasta que se presione una tecla
cv2.waitKey(0)

# Cerrar las ventanas de OpenCV
cv2.destroyAllWindows()