FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requierements.txt

RUN pip install --no-cache-dir -r requierements.txt

COPY . /app


EXPOSE 8001


#Run the application


CMD [ "uvicorn","main:app","--host","0.0.0.0","--port","8000" ]

