from multiprocessing import Process,Pipe


#2fa pipe
def f(child_conn):
    msg = twofa
    child_conn.send(msg)
    child_conn.close()

#flag Pipe
def g(child_conn):
    msg = flag
    child_conn.send(msg)
    child_conn.close()

class twofaHold():

    def __init__(self):
        self.flag = True
        self.twofa = None
    def set2fa(self, twofa):
        self.twofa = twofa
        self.flag = False
    def get2fa(self):
        return self.twofa
    def getflag(self):
        return self.flag
