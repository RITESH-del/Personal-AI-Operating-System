class Tool:
   # Class-level list to store instances
   _instances = []

   def __init__(self, name, description, args, func):
       self.name = name
       self.description = description
       self.args = args
       self.func = func
       Tool._instances.append(self)


   @classmethod
   def get_all_instances(cls):
        return cls._instances
   


tools = Tool.get_all_instances()
