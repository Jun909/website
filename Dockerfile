# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV UV_PYTHON_PREFERENCE=system

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.4 /uv /uvx /bin/

# Install Poetry
# Copy the project into the image
ADD . /app

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen

# Collect static files for Django
# RUN uv run manage.py collectstatic --noinput

# Expose the port that Django will run on
EXPOSE 8000

# Run the Django server
CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]

