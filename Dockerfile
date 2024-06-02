FROM python:latest

WORKDIR ./dev-media

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5005

CMD ./start_app.sh
