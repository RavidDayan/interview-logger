class Logger:
    def __init__(self):
        # holds messages by arrival order
        self.logList = []
        # key=message,value=timestamp
        self.logDic = {}

    def printer(self, timestamp, message):
        # remove all messages that more than 10 seconds have passed since they were printet
        while self.logList:
            if self.logDic[self.logList[0]] + 10 <= timestamp:
                self.logDic.pop(self.logList[0])
                self.logList.pop(0)
            else:
                break
        # after while loop the message should still be in dictionary if 10 seconds have not passed
        # otherwise,add message to dic and list.
        if message in self.logDic:
            return False
        else:
            self.logList.append(message)
            self.logDic[message] = timestamp
            return True


