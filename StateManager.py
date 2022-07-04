from typing import Callable, Dict,Any, Tuple, Union
def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
            print("Created new instance of {}".format(class_))

        return instances[class_]

    return getinstance


@singleton
class StateManager:
    """
    Global State management and persistance.
    """
    def __init__(self):
        self.store:Dict[str,Any] = dict()


    def __getitem__(self, key:str) ->Union[Any,None]:
        if self.__contains__(key):
            return self.store[key]
        return None 

    def __setitem__(self, key:str, value:Any) ->None:
        self.store[key] = value

    def __delitem__(self, key:str)->None:
        del self.store[key]

    def __contains__(self, key:str)->bool:
        return key in self.store

    def __len__(self)->int:
        return len(self.store)
    
    def readFile(self, path:str) ->str :
        with open(path, "r") as f:
            return f.read()

    def writeFile(self, path)->int:
        with open(path, "w") as f:
            return f.write()
    