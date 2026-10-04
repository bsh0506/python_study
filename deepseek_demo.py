"""
DeepSeek API 调用示例（思考模式）

API Key 的配置方式（按优先级）：
    1. 系统环境变量 DEEPSEEK_API_KEY（已存在则优先使用）
    2. 同目录下的 .env 文件（推荐，见 .env.example 模板）

准备 .env 文件：
    cp .env.example .env
    然后编辑 .env 填入真实 key

API Key 申请地址：https://platform.deepseek.com/api_keys
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# ------------------------------------------------------------------
# 加载 .env 文件
# 用 Path(__file__) 拼出绝对路径，这样无论在哪个目录运行都能找到 .env，
# 不会出现"在 PyCharm 里能跑、在终端里找不到变量"的问题。
# load_dotenv 默认不覆盖已存在的环境变量，所以系统环境变量优先级更高。
# ------------------------------------------------------------------
ENV_FILE = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ENV_FILE)

# ------------------------------------------------------------------
# 读取 API Key
# 注意：os.environ.get() 的参数是「环境变量的名字」，不是 key 本身。
# 这里传的是变量名 "DEEPSEEK_API_KEY"，绝不能把 sk- 开头的真实 key 写进来。
# ------------------------------------------------------------------
api_key = os.environ.get("DEEPSEEK_API_KEY")

if not api_key:
    print("❌ 未找到 DEEPSEEK_API_KEY", file=sys.stderr)
    print(file=sys.stderr)
    print(f"已尝试从环境变量和 {ENV_FILE.name} 读取，都没有找到。", file=sys.stderr)
    print(file=sys.stderr)
    print("解决办法：在同目录创建 .env 文件并填入 key：", file=sys.stderr)
    print("    cp .env.example .env", file=sys.stderr)
    print("    # 然后编辑 .env，把 sk-your-key-here 换成你的真实 key", file=sys.stderr)
    print(file=sys.stderr)
    print("API Key 申请地址：https://platform.deepseek.com/api_keys", file=sys.stderr)
    sys.exit(1)

if api_key.startswith("sk-把你的") or api_key == "sk-your-key-here":
    print("❌ .env 文件里的 key 还是占位符，请填成真实 key", file=sys.stderr)
    print(f"    文件位置：{ENV_FILE}", file=sys.stderr)
    sys.exit(1)

# ------------------------------------------------------------------
# 创建客户端
# DeepSeek 兼容 OpenAI 接口，所以复用 openai 库，只改 base_url。
# ------------------------------------------------------------------
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)

# ------------------------------------------------------------------
# 发起请求（思考模式）
#   reasoning_effort="high"                        思考强度
#   extra_body={"thinking": {"type": "enabled"}}   开启思考模式
# 文档：https://api-docs.deepseek.com/zh-cn/guides/thinking_mode/
# ------------------------------------------------------------------
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)

message = response.choices[0].message

# ------------------------------------------------------------------
# 输出结果
# 思考模式下：思维链在 reasoning_content 里，最终答案在 content 里。
# reasoning_content 只在开启思考模式时才有值，用 getattr 做兼容处理。
# ------------------------------------------------------------------
reasoning = getattr(message, "reasoning_content", None)

if reasoning:
    print("=" * 60)
    print("【思考过程】")
    print("=" * 60)
    print(reasoning)
    print()

print("=" * 60)
print("【最终回答】")
print("=" * 60)
print(message.content)

# 可选：查看本次调用的 token 消耗
if response.usage:
    print()
    print("-" * 60)
    print(f"输入 tokens: {response.usage.prompt_tokens}")
    print(f"输出 tokens: {response.usage.completion_tokens}")
    print(f"合计 tokens: {response.usage.total_tokens}")
