class DB:
    def __init__(self,host=None,port=None,username=None,password=None,database=None):
        self.host=host 
        self.port=port 
        self.username=username
        self.password=password
        self.database=database

class DBBuilder:
    def __init__(self,host=None,port=None,username=None,password=None,database=None):
        self.host=host 
        self.port=port 
        self.username=username
        self.password=password
        self.database=database
    
    def set_host(self,new):
        self.host=new
        return self
    def set_port(self,new):
        self.port=new
        return self
    def set_username(self,new):
        self.username=new
        return self
    def set_password(self,new):
        self.password=new
        return self
    def set_database(self,new):
        self.database=new
        return self
    def build(self):
        if None in (self.host,self.port,self.database):
            raise ValueError("host, port and database must not to be empty")
        else:
            return DB(self.host,self.port,self.username,self.password,self.database)
        
builder = DBBuilder()

builder.set_host("localhost")
builder.set_port(5432)
builder.set_database("shop")

connection1 = builder.build()

builder.set_host("production-server")

connection2 = builder.build()

print(connection1.host)
print(connection2.host)