# Backend

## 快速启动

默认会使用免费的 Pollinations OpenAI-compatible 接口，不需要先创建 `backend/.env`。

```bash
conda create -n leetcode_env python=3.8.20
conda activate leetcode_env
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## 高级：自定义 API

只有需要切换供应商、模型或私有网关时，才需要在 `backend/.env` 中配置：

```env
# backend/.env

APP_LANGUAGE=zh

# 可选：default/free/pollinations, openai, deepseek, siliconflow, custom
LLM_PROVIDER=pollinations
LLM_MODEL=openai
```

### 使用内置供应商

```env
LLM_PROVIDER=siliconflow
SILICONFLOW_API_KEY=sk-your-siliconflow-key
LLM_MODEL=Qwen/Qwen2.5-72B-Instruct
```

也可以使用：

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-openai-key
LLM_MODEL=gpt-4o
```

```env
LLM_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-your-deepseek-key
LLM_MODEL=deepseek-chat
```

### 使用任意 OpenAI-compatible 网关

```env
LLM_PROVIDER=custom
LLM_BASE_URL=https://your-api.example.com/v1
LLM_API_KEY=sk-your-custom-key
LLM_MODEL=your-model-name
```
