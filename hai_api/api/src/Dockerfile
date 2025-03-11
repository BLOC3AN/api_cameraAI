# Sử dụng Python 3.8
FROM python:3.8-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy toàn bộ mã nguồn vào container
COPY . /app

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt && cd src/

# Mở cổng cho ứng dụng (nếu chạy API trên Flask/FastAPI)
EXPOSE 5000

WORKDIR /app/src
# Chạy ứng dụng
CMD ["python", "app.py"]
