import asyncio
from tiotr.message import Message

class Workspace:
    def __init__(self, verbose = True):
        self.mailbox = {}
        self.agents = []
        self.verbose = verbose

    async def register(self, agent):
        self.agents.append(agent)
        if agent.id not in self.mailbox.keys():
            self.mailbox[agent.id] = []

    async def check_message(self, agent):
        if len(self.mailbox[agent.id]) > 0:
            message = self.mailbox[agent.id][0]
            self.mailbox[agent.id].remove(message)
            return message
        return None

    async def send_message(self, sender_id, receiver_id, content):
        if receiver_id in self.mailbox.keys():
            self.mailbox[receiver_id].append(Message(sender_id, receiver_id, content))
        else:
            self.mailbox[receiver_id] = []
            self.mailbox[receiver_id].append(Message(sender_id, receiver_id, content))