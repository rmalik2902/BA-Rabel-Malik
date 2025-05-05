import os
from pdf2image import convert_from_path
from PIL import Image
import uuid

# Funktion: PDF in Bilddateien (max. 10 Seiten) umwandeln
def convert_pdf_to_images(pdf_path: str, output_folder: str = "app/temp_images", dpi: int = 300) -> list[str]:
    # Maximal 10 Seiten aus der PDF konvertieren
    images = convert_from_path(pdf_path, dpi=dpi, first_page=1, last_page=10)
    os.makedirs(output_folder, exist_ok=True)
    image_paths = []

    for i, image in enumerate(images):
        filename = f"{uuid.uuid4().hex}_page_{i+1}.png"
        full_path = os.path.join(output_folder, filename)
        image.save(full_path, "PNG")
        image_paths.append(full_path)

    return image_paths
