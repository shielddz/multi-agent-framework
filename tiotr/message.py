class Message:
    def __init__(self, sender, receiver, content):
        self.__sender = sender
        self.__receiver = receiver
        self.__content = content
    
    def get_sender(self):
        return self.__sender
    def get_receiver(self):
        return self.__receiver
    def get_content(self):
        return self.__content