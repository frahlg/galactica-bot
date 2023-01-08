FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]