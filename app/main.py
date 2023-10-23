import fitz  # PyMuPDF
import os

def insert_signature(pdf_path, image_path, output_path, coordinates, scale_factor=1.0):
    # Carga el PDF
    pdf_document = fitz.open(pdf_path)

    # Obtiene la página y sus dimensiones que deseas firmar
    page = pdf_document.load_page(2)
    page_width = page.rect.width
    page_height = page.rect.height

    # Calcula la posición para insertar la imagen
    x, y = coordinates
    x = x * page_width
    y = (1 - y) * page_height

    # Carga la imagen a insertar
    image = fitz.open(image_path)
    image_page = image.load_page(0)

    # Obtiene las dimensiones originales de la imagen
    image_width = image_page.rect.width
    image_height = image_page.rect.height

    # Calcula las nuevas dimensiones de la imagen utilizando el factor de escala (scale_factor)
    new_image_width = image_width * scale_factor
    new_image_height = image_height * scale_factor

    # Establece la posición de la imagen
    image_rect = fitz.Rect(x, y, x + new_image_width, y + new_image_height)

    # Sobrepone la imagen en la página con las nuevas dimensiones
    page.insert_image(image_rect, pixmap=image_page.get_pixmap(), overlay=True)

    # Guarda el pdf con las imagenes insertadas
    pdf_document.save(output_path)
    pdf_document.close()

def process_files_in_folder(input_folder, output_folder, image_path, scale_factor=1.0):
    # Obtiene la lista de archivos en la carpeta de entrada
    files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    for file_name in files:
        # Ruta completa al archivo de entrada
        input_file_path = os.path.join(input_folder, file_name)

        # Ruta completa para el archivo de salida
        output_file_path = os.path.join(output_folder, f"{file_name}")

        # Coordenadas y escala de la imagen (ajusta según sea necesario)
        coordinates = (0.68, 0.355)  # Ajusta estas coordenadas para cada PDF

        # Inserta la firma en la tercera página del archivo
        insert_signature(input_file_path, image_path, output_file_path, coordinates, scale_factor)

# Rutas de las carpetas y la imagen
input_folder = 'tu ruta de archivos a modificar'  # Carpeta de entrada
output_folder = 'tu ruta donde iran a parar tus archivos modificados'  # Carpeta de salida
image_path = 'tu ruta de la imagen a insertar'  # Ruta de la imagen de la firma

# Escala para el tamaño de la imagen (ajusta según sea necesario)
scale_factor = 0.35

# Procesa los archivos en la carpeta
process_files_in_folder(input_folder, output_folder, image_path, scale_factor)