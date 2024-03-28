FROM python:latest
WORKDIR /code
ADD . /code
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5001
CMD ["python", "app.py"]


