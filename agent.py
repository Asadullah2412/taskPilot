import os
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from tools import tools
from langchain.agents import create_agent


# loads local variables
load_dotenv() 



model = ChatOpenRouter(
    # model= 'liquid/lfm-2.5-2.6b:free', // change the model as per availabilty
    model = "inclusionai/ling-3.0-flash-sante:free"
)

agent = create_agent(
    model=model,
    tools =tools
)




import asyncio

# 1. Change 'def' to 'async def'
async def run_agent(question: str):
    """Run the agent and print a clean, beginner-friendly execution trace."""

    print(f"\n🧑 User: {question}")
    print("-" * 60)

    # 2. Add 'await' right here!
    result = await agent.ainvoke({
        "messages": [("user", question)]
    })

    print("🔎 Clean Agent Execution Trace")
    print("-" * 60)

    step = 1
    for msg in result["messages"]:
        # 1. Human message = original user question
        if msg.type == "human":
            print(f"{step}. User asked:")
            print(f"   {msg.content}")
            step += 1

        # 2. AI message with tool_calls = agent decided to use a tool
        elif msg.type == "ai" and getattr(msg, "tool_calls", None):
            for tool_call in msg.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]

                print(f"{step}. Agent decision:")
                print(f"   I need to use the tool: {tool_name}")
                print(f"   Tool input: {tool_args}")
                step += 1

        # 3. Tool message = result returned by the tool
        elif msg.type == "tool":
            print(f"{step}. Tool observation:")
            print(f"   Tool returned: {msg.content}")
            step += 1

        # 4. Final AI message = final response to user
        elif msg.type == "ai" and msg.content:
            print(f"{step}. Final answer:")
            print(f"   {msg.content}")
            step += 1

    print("=" * 60)


# 3. Use asyncio.run() to execute the async function at the bottom of your file
# asyncio.run(
#     run_agent("today im planing to play football , then go for a dinner and take a bath and have a good sleep ,add these tasks "
#               )
# )

asyncio.run(
    run_agent("i have played football , took a bath and ate dinner and i am going to sleep and also i have done typescript too so remove these tasks "
              )
)
