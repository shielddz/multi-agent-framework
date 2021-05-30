import asyncio
from time import perf_counter as pc
class Agent():
    def __init__(self, agent_id, workspace):
        self.id = agent_id
        self.workspace = workspace
        self.behaviours = []

    async def start(self):
        # Subscribing to the workspace
        await self.workspace.register(self)

        # Waiting for the setup completion
        await self.setup()

        # Run the behaviours sequentially
        while True:
            for behaviour in self.behaviours:
                if not behaviour.is_running:
                    await behaviour.start()

    def add_behaviour(self, behaviour):
        self.behaviours.append(behaviour)
        behaviour.agent = self

    async def check_message(self, timeout):
        tic = pc()
        while True:
            message = await self.workspace.check_message(self)
            await asyncio.sleep(0)
            if message:
                return message
            tac = pc()
            if tac - tic > timeout:
                return None

    async def send_message(self, receiver_id, content):
        await self.workspace.send_message(self.id, receiver_id, content)

    # To Implement
    async def setup(self):
        print(self.id)
        await asyncio.sleep(1)
        
    def stop(self):
        for behaviour in self.behaviours:
            behaviour.kill()