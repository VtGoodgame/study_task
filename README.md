### Study task
Study task является минимальным backend-проектом на FastAPI, который запускается в Docker-контейнере.


## 📋 Требования
- Docker и Docker Compose
- Python 3.12+ (для локального запуска)

## 🏗️ Архитектура проекта

```
study_task/
├── app/                         # Основное приложение
│   ├── main.py                  # Точка входа, основной цикл
│   ├── consts.py                # Загрузка переменных из .env   
│   ├── .dockerignore            # Docker образ для приложения
│   ├── requirements.txt         # Python зависимости
│   │
│   ├── routers/                 
│   │   ├── files.py             # router возвращающий список файлов текущего проекта через Python.
│   │   ├── health.py            # router для проверки состояния сервера
│   │   └── version.py           # router возвращающий версию апи
│   │
│   └── scripts/
│       └── path.py              #  функция возвращающая список файлов текущего проекта
│
├── docker-compose.yml           # Конфигурация Docker Compose
├── run.sh                       # Bash скрипт для локального запуска проекта
├── .env                         # Переменные окружения
└── README.md                    # Этот файл
```

### 1️⃣ Запуск с Docker (рекомендуется)

1. **Собрать образ**
```bash
docker-compose build --no-cache
```

2. **Запуск образа**
```bash
docker-compose up
```

### 3️⃣ Запуск локально (без Docker)

**Создание виртуального окружения:**
```bash
bash run.sh
```
> **Примечание**: 
локальный запуск происходит с использованием bash скрипта. Для windows требуется установка терминала подобному gitbash.

---
**Последнее обновление:** 18/07/2026

**Python версия:** 3.12

**Docker:** требуется Docker и Docker Compose
