
docker pull python:3.11-slim


# 建構 Docker 映像, base python:3.11-slim, 再依照Dockerfile
# 內容，建一個新的image
docker build -t my-llm-app .

# 啟動容器
docker run --rm -it my-llm-app


# LLM image
docker run -d --name llama -p 8000:8000 nvcr.io/nim/meta/llama-3.1-8b-instruct:1.1.2
