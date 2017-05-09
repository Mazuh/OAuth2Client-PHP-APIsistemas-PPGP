"""
All DAOs should be called using this module, instead
of directly call their own constructor.

A factory of Data Access Objects.
"""

from .dao import DAO

# constants for collection names in mongodb

COLLECTION_OF_USERS = 'users'
COLLECTION_OF_POST_GRADUATIONS = 'postGraduations'

# factory methods

#def get_user_dao():
#    """ Get a user DAO instance. (TODO: implement some kind of singleton) """
#    return DAO(COLLECTION_OF_USERS)

def post_graduation_dao():
    """ Get a user DAO instance. (TODO: implement some kind of singleton) """
    return DAO(COLLECTION_OF_POST_GRADUATIONS)
