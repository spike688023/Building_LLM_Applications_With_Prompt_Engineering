FROM python:3.11-slim

WORKDIR /app

# 安裝系統依賴（gcc、curl 可選，某些套件需要編譯）
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Python 套件
RUN pip install --no-cache-dir \
    langchain \
    langchain-nvidia-ai-endpoints \
    pydantic

# 複製程式碼
COPY . .

# 預設執行你的 Python 腳本
CMD ["python", "run_llm.py"]

