# lime-agent
Private local RAG AI Shopping Assistant for cross-border e-commerce.

# --reload 表示修改代码后服务器会自动热重启，开发极其方便
uv run uvicorn lime_agent.main:app --reload --port 8000

rag-shopping-assistant/
├── backend/                  # 后端：Python RAG 核心（FastAPI + LlamaIndex/LangChain）
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # 后端主入口（API 路由、CORS 配置）
│   │   ├── config.py         # 配置文件（模型选择、路径、密钥等）
│   │   ├── core/             # RAG 核心逻辑
│   │   │   ├── __init__.py
│   │   │   ├── engine.py     # 问答与检索控制流（Query Engine / Chat Engine）
│   │   │   └── pipeline.py   # 数据流：文档切块、Embedding、索引构建
│   │   ├── database/         # 向量数据库及本地缓存
│   │   │   └── chroma_store/ # ChromaDB 向量数据持久化本地目录（自动生成）
│   │   └── templates/        # 核心 Prompt 模板管理
│   │       └── system_prompts.py # 锁死 AI 销售人设与不准幻觉的 Prompt
│   ├── data/                 # 本地知识库（把老板的说明书扔这里）
│   │   ├── mock_erp.json     # 模拟的商品库存、货代物流数据（用于惊艳老板）
│   │   └── raw_docs/         # 存放扒下来的英文产品 PDF / Markdown 说明书
│   │       └── product_manual.md
│   ├── requirements.txt      # Python 依赖包（FastAPI, llama-index, ollama, chromadb 等）
│   └── .env                  # 后端环境变量
│
├── frontend/                 # 前端：Next.js 全栈客服/导购聊天组件
│   ├── public/               # 静态资源（假装是某个大牌独立站的 Logo）
│   │   └── favicon.ico
│   ├── src/
│   │   ├── app/              # Next.js App Router 架构
│   │   │   ├── layout.tsx    # 全局布局
│   │   │   ├── page.tsx      # 主页面（假装是一个精美的商品落地页）
│   │   │   └── api/          # 前端 BFF 层（可选，可直接直连后端 FastAPI）
│   │   ├── components/       # 核心前端组件
│   │   │   ├── ChatWidget.tsx # 独立站右下角的“悬浮聊天气泡”
│   │   │   ├── ChatWindow.tsx # 丝滑的聊天对话窗口（支持 Streaming 打字机效果）
│   │   │   └── MessageItem.tsx# 单条消息（区分用户、AI、以及触发的“优惠券卡片”）
│   │   └── hooks/
│   │       └── useChat.ts    # 封装聊天状态、WebSocket 或 Stream 流式传输逻辑
│   ├── package.json          # Node.js 依赖（TailwindCSS, Lucide-react 等）
│   ├── tailwind.config.js    # 样式配置（方便一键切成老板网站的品牌色）
│   └── .env.local            # 前端本地环境配置
│
└── README.md                 # 极客自修手册 / 准备去对线时的演示指南
