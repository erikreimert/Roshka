class twofaHold():

    def __init__(self):
        self.flag = True
        self.twofa = None
        # self.test = '\nfunca oluo\n'
    def set2fa(self, twofa):
        self.twofa = twofa
        self.flag = False
    def get2fa(self):
        return self.twofa
    # def getTest(self):
    #     return self.test
    def getflag(self):
        return self.flag
