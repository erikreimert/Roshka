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
