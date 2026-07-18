FROM python:3.11-slim@sha256:5e38a2d4e18bdad0ad1a10ba5f23e8cc6d4c11fad9d1a901ebf0f6eb9ca0b8a8

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
