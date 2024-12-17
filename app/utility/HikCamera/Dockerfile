FROM python:3.10-slim
COPY . /test
WORKDIR /test
RUN dpkg -i /test/MvCamCtrlSDK_Runtime-4.4.1_aarch64_20240827.deb
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 
ENV MVCAM_COMMON_RUNENV=/opt/MVS/lib LD_LIBRARY_PATH=/opt/MVS/lib/64:/opt/MVS/lib/32:$LD_LIBRARY_PATH PYTHONPATH=/hik_camera:$PYTHONPATH
RUN pip install --no-cache-dir --upgrade -r /test/requirements.txt --no-cache
CMD ["python3", "main.py"]
