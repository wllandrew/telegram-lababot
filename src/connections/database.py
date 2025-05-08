import env
from pymongo import MongoClient

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
       
        if not self.db.find_one({"_id" : id}):
            self.add_user(id)
            self.add_task(id, task_name, task_date)
            return
        elif self.check_task(id, task_name, task_date):
            raise Exception("Error in adding task: task already exists.")
        
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
    
    def remove_task(self, id : int, task_name : str, task_date : str):
        self.db.update_one({
                "_id" : id
            }, 
            { 
                "$pull" : { 
                    "tasks" : {
                        "name" : task_name,
                        "date" : task_date
                    }
                } 
            })

    def check_task(self, id : int, task_name : str, task_date : str):
        return self.db.find_one({
                "_id" : id,
                "tasks" : {
                    "name" : task_name,
                    "date" : task_date
                },
            })
    
    def get_tasks(self, id : int):
        return self.db.find_one({
                "_id" : id
            }, 
            {
                "tasks": 1
            })

    def add_test(self, id : int, test_name : str, test_date : str):
        if not self.db.find_one({"_id" : id}):
            self.add_user(id)
            self.add_test(id, test_name, test_date)
            return
        elif self.check_test(id, test_name, test_date):
            raise Exception("Error in adding test: test already exists.")
        
        self.db.update_one({
                "_id" : id
            }, 
            { 
                "$push" : { 
                    "tests" : {
                        "name": test_name,
                        "date" : test_date
                    }
                } 
            })
    
    def remove_test(self, id : int, test_name : str, test_date : str):
        self.db.update_one({
                "_id" : id
            }, 
            { 
                "$pull" : { 
                    "tests" : {
                        "name" : test_name,
                        "date" : test_date
                    }
                } 
            })
        
    def check_test(self, id : int, test_name : str, test_date : str):
        return self.db.find_one({
                "_id" : id,
                "tests" : {
                    "name" : test_name,
                    "date" : test_date
                },
            })
    
    def get_tests(self, id : int):
        return self.db.find_one({
                "_id" : id
            }, 
            {
                "tests": 1
            })
    
DB = DbConnection()
