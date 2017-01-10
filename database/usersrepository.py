from functools import wraps

from database.clientconfigurator import ClientConfiguration
from database.user_decorator import user_decorator

class UserRepository:
    user_collection = ClientConfiguration.get_client().cemappdb.users

    @classmethod
    def insert(cls, user_data):
        cls.user_collection.insert_one(user_data)

    @user_decorator
    def get_user(user_id):
        return UserRepository.user_collection.find_one({"user_id": user_id})



