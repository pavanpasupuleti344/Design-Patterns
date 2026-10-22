class Config:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance 
    

    def __init__(self):
        if not hasattr(self,'reg'):
            self.db='noSql'
            self.env='Developed'
            self.reg=True

s1=Config()

s2=Config()

print(s1 is s2)
print(s1.db)
s1.db='MySQL'
s3=Config()
print(s3.db)
print(s2 is s3)