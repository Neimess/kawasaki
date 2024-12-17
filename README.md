# Проект: Обработка изображений с видеопотока на основе FastAPI

## Описание

Проект предназначен для обработки видеопотока с камер, включая детекцию, классификацию объектов и обработку изображений. Разработка основывается на FastAPI и включает несколько модулей для обработки изображений, работы с SDK камер и API маршрутизации.

---

## Структура проекта

```
├── docker-compose.yml        # Конфигурация Docker Compose
├── .env_vars                 # Файл переменных окружения
├── app/
│   ├── Dockerfile            # Dockerfile для сборки приложения
│   ├── main.py               # Точка входа FastAPI
│   ├── requirements.txt      # Зависимости проекта
│   ├── services/             # Сервисы и обработка данных
│   │   ├── camera.py         # Работа с камерами
│   │   ├── image_processor.py # Обработка изображений
│   │   ├── detection.py      # Логика детекции объектов
│   ├── models/               # Модели для предсказаний
│   │   ├── model_loader.py   # Загрузка ML модели
│   │   ├── prediction.py     # Предсказание объектов
│   ├── api/                  # API маршруты
│   │   ├── routers/          # Маршруты FastAPI
│   │       ├── predict.py    # Роут для предсказаний
│   │       ├── camera_router.py # Роут для работы с камерами
│   ├── utility/              # Утилиты и SDK
│   │   ├── HikCamera/        # SDK для работы с камерами Hikvision
├── config/nginx/nginx.conf   # Конфигурация Nginx
└── README.md                 # Документация
```

---

## Установка и запуск проекта

### Шаги для запуска:

1. **Клонирование репозитория**:

   ```bash
   git clone <>
   cd <>
   ```

2. **Создание `.env` файла**:
   Скопируйте `.env_vars` и настройте переменные окружения.

3. **Сборка и запуск через Docker Compose**:

   ```bash
   docker-compose up --build
   ```

4. **Доступ к API**:
   API будет доступен по адресу: `http://localhost:8000`

---

## Функциональность

1. **Обработка видеопотока**:
   - Захват видеопотока с камер.
   - Обработка изображений (контурная детекция, предсказания объектов).
2. **API на FastAPI**:
   - `/predict` - эндпоинт для выполнения предсказаний на изображении.
   - `/camera` - эндпоинт для взаимодействия с камерами.
3. **Поддержка работы с SDK камер Hikvision**.
4. **Докеризация проекта**.
5. **Реверс-проксирование через Nginx**.

---

## Задачи и распределение работы

### Разработчик 1: Игорь Варламов

1. **Архитектура проекта**:
   - Создание каркаса FastAPI приложения.
   - Настройка API маршрутов (`api/routers/...`).
2. **Сервисы**:
   - Модуль для работы с камерами (`services/camera.py`).
   - Обработка изображений (`services/image_processor.py`).
3. **Модули машинного обучения**:
   - Загрузка и инициализация модели (`models/model_loader.py`).
   - Реализация предсказаний (`models/prediction.py`).

### Разработчик 2: Максим Гавриленко

1. **Интеграция SDK камер**:
   - Работа с SDK камер Hikvision (`utility/HikCamera/...`).
   - Добавление утилит для управления камерами.
2. **Nginx конфигурация**:
   - Настройка проксирования через `config/nginx/nginx.conf`.
3. **Докеризация**:
   - Написание `Dockerfile` и `docker-compose.yml`.

---

## Зависимости

Проект использует следующие технологии и библиотеки:

- **FastAPI**: для построения REST API.
- **Docker и Docker Compose**: для контейнеризации.
- **PyTorch**: для загрузки и работы с ML моделями.
- **Nginx**: для проксирования запросов.
- **Hikvision SDK**: для работы с камерами.

Установите зависимости:

```bash
pip install -r app/requirements.txt
```

---

## Контакты

- **Игорь Варламов**: froginkrit@gmail.com
- **Максим Гавриленко**: maksimgavrilenkowork@gmail.com

---
