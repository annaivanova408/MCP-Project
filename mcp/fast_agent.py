import asyncio
from mcp_agent.core.request_params import RequestParams
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("fast-agent agent_one (mcp server)")



# Define the agent
@fast.agent(name="agent_one",
            instruction="You are a helpful AI Agent.",
            model='generic.qwen3:1.7b',
            servers=["agent_one"],
            request_params=RequestParams(
                maxTokens=8192,
                use_history=False,
                max_iterations=20,
            )
        )
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())