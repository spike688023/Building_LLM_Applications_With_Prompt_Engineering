import json, os

from typing import List
from pprint import pprint

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel, Field

# 連到你本機或容器內的 LLM 推理服務

os.environ["NVIDIA_API_KEY"] = "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"
llm = ChatNVIDIA(model="meta/llama3-8b-instruct", api_key=os.environ["NVIDIA_API_KEY"])

# llm = ChatNVIDIA(base_url=base_url, model=model, temperature=0)
response = llm.invoke("Hello, world!")
print(response)

