import fitz  # PyMuPDF
import os

def insert_signature(pdf_path, image_path, output_path, coordinates, scale_factor=1.0):
    # Load the PDF
    pdf_document = fitz.open(pdf_path)

    # Get the third page and its dimensions
    page = pdf_document.load_page(2)
    page_width = page.rect.width
    page_height = page.rect.height

    # Calculate the position to insert the image
    x, y = coordinates
    x = x * page_width
    y = (1 - y) * page_height

    # Load the image
    image = fitz.open(image_path)
    image_page = image.load_page(0)

    # Get the original image dimensions
    image_width = image_page.rect.width
    image_height = image_page.rect.height

    # Calculate the new image dimensions using the scale_factor
    new_image_width = image_width * scale_factor
    new_image_height = image_height * scale_factor

    # Set the position of the image
    image_rect = fitz.Rect(x, y, x + new_image_width, y + new_image_height)

    # Overlay the image on the page with the new dimensions
    page.insert_image(image_rect, pixmap=image_page.get_pixmap(), overlay=True)

    # Save the modified PDF with the inserted image
    pdf_document.save(output_path)
    pdf_document.close()

def process_files_in_folder(input_folder, output_folder, image_path, scale_factor=1.0):
    # Obtén la lista de archivos en la carpeta de entrada
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
input_folder = 'C:\\Users\\israe\\OneDrive\\Desktop\\Contratos'  # Carpeta de entrada
output_folder = 'C:\\Users\\israe\\OneDrive\\Desktop\\Modificados'  # Carpeta de salida
image_path = 'C:\\Users\\israe\\Downloads\\firma.png'  # Ruta de la imagen de la firma

# Escala para el tamaño de la imagen (ajusta según sea necesario)
scale_factor = 0.35

# Procesa los archivos en la carpeta
process_files_in_folder(input_folder, output_folder, image_path, scale_factor)