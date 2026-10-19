FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd --create-home appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py tasks.py display.py storage.py ./
RUN mkdir -p /app/data && chown -R appuser:appuser /app

USER appuser

VOLUME ["/app/data"]

ENTRYPOINT ["python", "main.py"]
CMD ["list"]