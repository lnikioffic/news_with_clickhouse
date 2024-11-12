FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod a+x /app/docker/app.sh

ENTRYPOINT ["sh", "app.sh"]