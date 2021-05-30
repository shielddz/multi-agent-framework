import asyncio

class Behaviour:
    def __init__(self):
        self.is_running = False

    async def start(self):
        self.is_running = True
        await self.on_start()
        while(True):
            await self.run()
            if not self.is_running:
                break
        await self.on_end()

    def kill(self):
        self.is_running = False

    async def wait_message(self, timeout=0):
        return await self.agent.check_message(timeout)

    async def send_message(self, receiver_id, content):
        await self.agent.send_message(receiver_id, content)


    # To implement
    async def on_start(self):
        await asyncio.sleep(0)

    async def run(self):
        await asyncio.sleep(0)

    async def on_end(self):
        await asyncio.sleep(0)