class Message:
    def __init__(self,len,price1,price2):
        self.message_len = len
        self.message_p1 = price1
        self.message_p2 = price2
    def price(self, text):
        print(text)
        if len(text) <= self.message_len:
            result = (self.message_p1)
            print(result)
        elif len(text) > self.message_len:
            result = (self.message_p2)
            print(result)

    my_message = Message(5,50,1000)
    my_message.price("현대건설 안전관리")
