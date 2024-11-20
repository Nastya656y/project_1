# Backup Script
## Авторы:


## Описание
Этот проект представляет собой Python-скрипт для автоматического создания резервных копий указанных директорий. Бэкапы сохраняются в заданную директорию назначения с уникальными временными метками. Скрипт работает в фоновом режиме и выполняет бэкапы через указанные интервалы времени.
### Структура проекта
```
backup_script/
│
├── main.py           # Основной файл запуска программы
├── backup.py         # Модуль для выполнения операций бэкапа
├── scheduler.py      # Модуль для управления периодическим выполнением бэкапов
└── config.json       # Файл конфигурации
```
### Конфигурация
```json
{
    "directories_to_backup": ["D:/path/to/source1", "D:/path/to/source2"],
    "backup_destination": "D:/path/to/destination",
    "backup_period": 3600,
    "log_level": "INFO"
}
```
- ```directories_to_backup```: Список директорий для резервного копирования.
- ```backup_destination```: Путь к директории, где будут сохраняться резервные копии.
- ```backup_period```: Интервал между резервными копиями в секундах.
- ```log_level```: Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL).
### Использование
1. Убедитесь, что файл ```config.json``` настроен и находится в одной директории с ```main.py```.
2. Запустите скрипт:
```bash
python main.py
```
3. Программа автоматически создаст бэкапы через указанные интервалы времени.
4. Чтобы остановить скрипт, нажмите ```Ctrl+C```.
### Требования
- Python 3.10+
- ОС: Windows, macOS, Linux