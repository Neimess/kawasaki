# Используем официальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY . . 

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade -r requirements.txt --no-cache
 
# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && dpkg -i /app/utility/MvCamCtrlSDK_Runtime-4.4.1_aarch64_20240827.deb || apt-get install -f -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /app/utility/MvCamCtrlSDK_Runtime-4.4.1_aarch64_20240827.deb
ENV MVCAM_COMMON_RUNENV=/opt/MVS/lib LD_LIBRARY_PATH=/opt/MVS/lib/64:/opt/MVS/lib/32:$LD_LIBRARY_PATH PYTHONPATH=/app:$PYTHONPATH
# Указываем команду запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
WORKDIR /
