FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN chmod a+x /app/docker/*.sh

# RUN python migration.py

# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]