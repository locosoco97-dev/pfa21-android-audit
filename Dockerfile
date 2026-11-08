FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /work
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Le depot est monte dans /work au lancement (voir Makefile)
CMD ["python", "scripts/check_env.py"]
