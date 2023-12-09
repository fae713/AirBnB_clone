#!/usr/bin/python3
""" This is the BaseModel Module"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel: A class BaseModel that defines all common
               attributes/methods for other classes..
    """

    def __init__(self, *args, **kwargs):
        """ This is the constructor method.
            It initializes every newly created object of the class.

            Attributes:
                *args: Arguments list.

                **kwargs: Keyworded arguments list.

                id (int): uuid of current instance.

                created_at (datetime): The current datetime when
                                       an instance is created.

                updated_at (datetime): The current datetime an
                                       instance was updated.

            Methods:
                save(): To save the files.
                to_json(): To convert saved files to JSON
        """

        self.id = str(uuid.uuid4())
        # Generates unique ID for 'uuid.uuid4() and converts to a string
        self.created_at = datetime.now()
        # Sets the created_at attribute to the
        # current datetime the instance is created.
        self.updated_at = datetime.now()
        # Sets the updated_at attribule to the
        # current datetime the instance is updated.

        if len(kwargs) > 0:
            timeformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif (key == "created_at"):
                    self.created_at = datetime.strptime(value, timeformat)
                elif (key == "updated_at"):
                    self.updated_at = datetime.strptime(value, timeformat)
                else:
                    setattr(self, key, value)

        else:
            models.storage.new(self)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__>,
            which is the string representation of the object instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        To save data and update the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        the_dict = self.__dict__.copy()
        the_dict["created_at"] = self.created_at.isoformat()
        the_dict["updated_at"] = self.updated_at.isoformat()
        the_dict["__class__"] = self.__class__.__name__

        return the_dict
