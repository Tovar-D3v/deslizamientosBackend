# 1. Imagen base
FROM python:3.11-slim

# 2. Variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Directorio de trabajo
WORKDIR /app

# 4. Instala dependencias del sistema para compilar mysqlclient Y AHORA GDAL/GEOS
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      pkg-config \
      default-libmysqlclient-dev \
      libssl-dev \
      # --- ¡AÑADE ESTAS LÍNEAS PARA GDAL Y GEOS! ---
      libgdal-dev \
      libgeos-dev \
      # ---------------------------------------------
 && rm -rf /var/lib/apt/lists/*

# 5. Copia e instala dependencias Python
COPY deslizamientos/requirements.txt /app/
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 6. Copia el código de tu proyecto
COPY deslizamientos/ /app/

# 7. Expone puerto y comando de arranque
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && daphne -b 0.0.0.0 -p 8000 deslizamientos.asgi:application"]