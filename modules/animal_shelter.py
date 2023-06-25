from pymongo import MongoClient

class AnimalShelter(object):
    """ 
    Class for performing CRUD operations on the Animal collection in MongoDB.
    """
    def __init__(self, username=None, password=None, hostname=None, port=None, database=None, collection=None):
        """
        Constructor method for the AnimalShelter class. Initializes the MongoDB client.
        
        Parameters:
        username (str): The username for MongoDB authentication. Default is None.
        password (str): The password for MongoDB authentication. Default is None.
        hostname (str): The hostname for MongoDB authentication. Default is None.
        port (str): The port for MongoDB authentication. Default is None.
        """
        if username and password and hostname and port and database and collection:
            try:
                self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, hostname, port))
                self.database = self.client['ACC']
                self.collection = self.database['animalsmodulesix'] # Need to update this
            except Execption as e:
                raise
        else:
            raise ValueError("Incomplete connection parameters. Please provide username, password, hostname and port.")

   
        
        
    def create(self, data):
        """
        Inserts a new document into the animals collection.

        Parameters:
        data (dict): The data to be inserted as a dictionary.

        Returns:
        True if insertion was successful, else the exception message.
        """
     
        if data is not None:
            try:
                insert = self.database.collection.insert_one(data)
                if insert != 0:
                    return True
                else:
                    return False
            except Exception as e:
                return str(e)       
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    def read(self, criteria=None):
        """
        Fetches documents from the collection.

        Parameters:
        criteria (dict): A dictionary specifying the query for the documents to be retrieved. Default is None.

        Returns:
        A cursor to the retrieved documents.
        """
        if criteria:
            data = self.database.animalsmodulesix.find(criteria, {"_id":False})
        else: 
            data = self.database.animalsmodulesix.find({}, {"_id":False})
        return data

        
    def update(self, query, data):
        try:
            result = self.database.collection.update_many(query, {'$set': data})
            return result.raw_result
        except Exception as e:
            return str(e)
        
#     def update(self, criteria=None):
#         """
#         Fetches documents from the animals collection.

#         Parameters:
#         criteria (dict): A dictionary specifying the query for the documents to be retrieved. Default is None.

#         Returns:
#         A cursor to the retrieved documents.
#         """
#         if criteria:
#             data = self.database.collection.find(criteria, {"_id":False})
#         else: 
#             data = self.database.collection.find({}, {"_id":False})
#         return data


    
#     def delete(self, criteria=None):
#         """
#         Fetches documents from the animals collection.

#         Parameters:
#         criteria (dict): A dictionary specifying the query for the documents to be retrieved. Default is None.

#         Returns:
#         A cursor to the retrieved documents.
#         """
#         if criteria:
#             data = self.database.collection.find(criteria, {"_id":False})
#         else: 
#             data = self.database.collection.find({}, {"_id":False})
#         return data
       # delete method  
    def delete(self, query):
        try:
            result = self.database.collection.delete_many(query)
            return result.raw_result
        except Exception as e:
            return str(e) 
    
    
    
    
    
    