# ── Base image ────────────────────────────────────────────────────────────────
FROM python:3.12-slim

# ── System deps + AWS CLI v2 (official installer) ─────────────────────────────
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        unzip \
        groff \
        less && \
    curl -fsSL "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o /tmp/awscliv2.zip && \
    unzip -q /tmp/awscliv2.zip -d /tmp && \
    /tmp/aws/install && \
    rm -rf /tmp/awscliv2.zip /tmp/aws && \
    apt-get remove -y curl unzip && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# ── App setup ─────────────────────────────────────────────────────────────────
WORKDIR /app

# Copy everything from the project folder into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ── Non-root user (security best practice) ────────────────────────────────────
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser /app
USER appuser

# ── Runtime config ────────────────────────────────────────────────────────────
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""
ENV AWS_DEFAULT_REGION="ap-south-1"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]