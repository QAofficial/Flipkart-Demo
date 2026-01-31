# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /workspace

# Install Robot Framework and Selenium (optional)
RUN pip install --no-cache-dir robotframework robotframework-seleniumlibrary selenium requests

# Optional: Install Chromium for Selenium tests
RUN apt-get update && \
    apt-get install -y chromium chromium-driver && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Default command: open bash
CMD ["bash"]
