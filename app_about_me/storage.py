# app_about_me/storage.py
from cloudinary_storage.storage import MediaCloudinaryStorage

"""
    Explicación: Esta pequeña clase PdfCloudinaryStorage hereda de MediaCloudinaryStorage (la clase base de Cloudinary para almacenar archivos) y en su inicializador (__init__), se asegura de que la opción resource_type siempre sea 'raw'.
"""

class PdfCloudinaryStorage(MediaCloudinaryStorage):
    """
    Custom storage for PDFs to ensure they are uploaded as 'raw' resources.
    """
    def __init__(self, **kwargs):
        # Llama al constructor de la clase padre primero
        super().__init__(**kwargs)
        # Asegúrate de que self.options esté inicializado y luego sobrescribe resource_type
        if self.options is None:
            self.options = {}
        self.options['resource_type'] = 'raw'