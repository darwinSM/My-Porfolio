# app_about_me/storage.py
from cloudinary_storage.storage import MediaCloudinaryStorage

_pdf_cloudinary_storage_instance = None

def get_pdf_cloudinary_storage():
    """
    Retorna una única instancia de MediaCloudinaryStorage configurada para recursos 'raw'.
    Esta función se usa como el argumento 'storage' en FileField/ImageField.
    """
    global _pdf_cloudinary_storage_instance
    if _pdf_cloudinary_storage_instance is None:
        # Creamos la instancia. Ahora encontrará CLOUDINARY_STORAGE en settings.py.
        _pdf_cloudinary_storage_instance = MediaCloudinaryStorage(resource_type='raw')
    return _pdf_cloudinary_storage_instance