class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.message_body = ""

    def get_sender(self):
        return self.sender

    def get_recipient(self):
        return self.recipient

    def append(self, text):
        self.message_body += text + "\n"

    def to_string(self):
        return f"From: {self.sender}\nTo: {self.recipient}\n{self.message_body}"


message = Message("Harry Morgan", "Rudolf Reindeer")

message.append("Hello Rudolf,")
message.append("How are you? I look forward to hearing from you soon.")
message.append("Best,")
message.append("Harry<3")

print(message.to_string())
