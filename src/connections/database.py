from pymongo import MongoClient
import env

class DbConnection:
    """
    Classe da conexão com o banco de dados MongoDB.
    Abstrai as operações e validações.
    """

    def __init__(self):
        self.cluster = MongoClient(f"mongodb+srv://admin:{env.MONGO_PASSWORD}@cluster0.trbbdxt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.cluster["Teste_Lababot"]
    
    def add_user(self, id : int):
        self.db.insert_one({
                "_id" : id, 
                "tasks" : [], 
                "tests" : []
            })
    
    def add_task(self, id : int, task_name : str):
        self.db.update_one({
                "_id" : id
            }, 
            { 
                "$push" : { 
                    "tasks" : task_name 
                } 
            })
    
    def remove_task(self, id : int, task_name : str):
        self.db.update_one({
                "_id" : id
            }, 
            { 
                "$pull" : { 
                    "tasks" : task_name 
                } 
            })

    def check_task(self, id : int, task_name : str):
        return len(self.db.find({
                "_id" : id,
                "tasks" : {
                    "$in" : [task_name]
                } 
            })) != 0
    
    def get_tasks(self, id : int):
        return self.db.find({
                "_id" : id
            }, 
            {
                "tasks", 1
            })
    
DB = DbConnection()
