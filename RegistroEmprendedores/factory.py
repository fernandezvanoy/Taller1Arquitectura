from django.conf import settings
from django.utils.module_loading import import_string

class StorageFactory:
    @staticmethod
    def create_storage():
        StorageClass = import_string(settings.IMAGE_STORAGE_CLASS)
        return StorageClass()
