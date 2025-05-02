# Use a lightweight Python base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir flask joblib scikit-learn

# Copy your app code and models
COPY app.py .
COPY score.py .
COPY models/ models/

# Expose the Flask port
EXPOSE 5000

# Launch the app
CMD ["python", "app.py"]

