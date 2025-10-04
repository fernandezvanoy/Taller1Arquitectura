import cloudinary.uploader

class ImageStorageInterface:
    "Interfaz para almacenamiento de imágenes"
    def upload(self, file, folder="products/"):
        raise NotImplementedError


class CloudinaryStorage(ImageStorageInterface):
    "Implementación real usando Cloudinary"
    def upload(self, file, folder="products/"):
        result = cloudinary.uploader.upload(file, folder=folder)
        return result.get("secure_url")
