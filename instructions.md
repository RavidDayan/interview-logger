#### Code template ####
class Logger:
    def __init__(self):
    # fill in missing code#

    def printer(self, timestamp:int, message:str):
    # fill in missing code#
####  The problem  ####
create a class callled Logger that has a function named printer.
printer(timestamp,message)-the printer function receives a timestamp and message ,the function returns true if the message has not been already received in the last 10 seconds and false otherwise
save as much memory space as you can
timestamps are given in accending order (i.e. timestamp1=t, timestamp2>=timestamp1 ....) 

####    Example    ####
logger=Logger()
logger.printer(1,'hello')->True
logger.printer(2,'bye')->True
logger.printer(3,'hello')->False
logger.printer(10,'hello')->False
logger.printer(11,'hello')->True
