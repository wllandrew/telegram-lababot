from pymongo import MongoClient
import env
from connections.exceptions.DatabaseException import DatabaseException

class DbConnection:
    """
    Classe da conexão com o banco de dados MongoDB.
    Abstrai as operações e validações.
    """

    def __init__(self):
        self.cluster = MongoClient(f"mongodb+srv://admin:{env.MONGO_PASSWORD}@cluster0.trbbdxt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.collection = self.cluster["Teste_Lababot"]
        self.db = self.collection["Users"]

    
    def add_user(self, id : int):
        self.db.insert_one({
                "_id" : id, 
                "tasks" : [], 
                "tests" : []
            })
    
    def add_task(self, id : int, task_name : str, task_date : str):
       
        if not self.db.find({"_id" : id}):
            DbConnection.add_user(id)
            DbConnection.add_task(id, task_name)
            return
        elif DbConnection.check_task(id, task_name, task_date):
            raise DatabaseException("Error in adding task: task already exists")
        
        self.db.update_one({
                "_id" : id
            }, 
            { 
                "$push" : { 
                    "tasks" : {
                        "name": task_name,
                        "date" : task_date
                    }
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

    def check_task(self, id : int, task_name : str, task_date : str):
        return len(self.db.find({
                "_id" : id,
                "tasks" : {
                    "name" : {"$in" : task_name},
                    "date" : {"$in" : task_date}
                },

            })) != 0
    
    def get_tasks(self, id : int):
        return self.db.find({
                "_id" : id
            }, 
            {
                "tasks", 1
            })
    
DB = DbConnection()
