from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse

# 加载根目录下的 .env
load_dotenv()

app = FastAPI(title="Lime Agent - RAG AI Shopping Assistant Backend")

# 允许跨境电商前端（如 Next.js 独立站开发环境）跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 实际生产环境建议缩窄到老板的独立站域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 定义前端传过来的请求体规范
class ChatRequest(BaseModel):
    message: str
    session_id: str


@app.get("/api/health")
def health_check():
    """供云端部署或本地检测健康状态使用"""
    return {"status": "healthy", "agent": "lime-agent"}


@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    """
    流式对话主接口
    前端只要往这里 POST 用户的问题，AI 就会流式吐出基于 LlamaIndex 检索说明书后的答案
    """
    try:
        # TODO: 这里后期对接 src/lime_agent/core/engine.py 的 LlamaIndex 检索流
        # 目前我们先写一个 Mock 的流式生成器，用来跑通前后端并网测试
        async def mock_rag_stream():
            reply = f"【青柠智能体】收到您的询问。关于您问的 '{request.message}'，正在检索本地产品说明书..."
            for char in reply:
                import asyncio

                await asyncio.sleep(0.05)  # 模拟 AI 思考和打字机速度
                yield {"data": char}
            yield {"data": "[DONE]"}  # 发送结束标记

        return EventSourceResponse(mock_rag_stream())

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
