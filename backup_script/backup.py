"""
Модуль для выполнения операций бэкапа.

Содержит функцию для копирования указанных директорий в директорию назначения.
Добавляет временную метку к именам папок, чтобы избежать перезаписи.
"""

import shutil
from pathlib import Path
import datetime
import logging

def perform_backup(source_dirs, destination_dir):
    """
    Выполняет копирование указанных директорий в директорию назначения.

    source_dirs -- Список путей к исходным директориям.
    destination_dir -- Путь к директории назначения.
    
    Функция реализована при помощи ChatGPT 4o mini
    """
    for source in source_dirs:
        source_path = Path(source)
        if not source_path.is_dir():
            logging.warning(f"Пропущено: {source} не является директорией.")
            continue
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        destination_path = Path(destination_dir) / f"{source_path.name}_backup_{timestamp}"
        
        try:
            shutil.copytree(source_path, destination_path)
            logging.info(f"Бэкап {source} успешно сохранен в {destination_path}.")
        except Exception as e:
            logging.error(f"Ошибка при бэкапе {source}: {e}")
