from rich.console import Console
from rich.traceback import install
from endecryption import encryption
from json import loads,dumps
from random import choice,sample,randint
from requests import get,post
install()
console = Console()
enc = encryption("fmwyeixiiqinwanryriojvzvpfwydqgr")

def req(data:dict) -> dict:
    while True:
        try: 
            response = post("https://messengerg2c58.iranlms.ir/",json=data).json()
            return loads(enc.decrypt(response["data_enc"]))
        except Exception as error:
            print(error)

def encrypt(json:dict,auth:str) -> dict:
    data = {
        "api_version" : "5",
        "auth" : auth,
        "data_enc" : enc.encrypt(dumps(json))
    }
    return req(data)

def changeId(id:str) -> None:
    json = {
        "method": "updateUsername",
        "input": {
            "username": id
        },
        "client": {
            "app_name": "Main",
            "app_version": "4.0.2",
            "platform": "Web",
            "package": "web.rubika.ir",
            "lang_code": "en"
        }
    }
    return encrypt(json,"fmwyeixiiqinwanryriojvzvpfwydqgr")
    
    
while True:
    def generatorIdRandom() -> str:
        generator = ''
        vache = ["a","b","c","d","e","f","g","h","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for index in range(0,randint(0,10)):
            generator += choice(vache)
        
        return generator
    
    console.log(changeId(generatorIdRandom()),log_locals=False)
    ...   
...