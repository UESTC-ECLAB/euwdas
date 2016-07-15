# -*- coding: utf-8 -*-

class UserMixin(object):
    '''
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    '''
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __eq__(self, other):
        '''
        Checks the equality of two `UserMixin` objects using `get_id`.
        '''
        if isinstance(other, UserMixin):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        '''
        Checks the inequality of two `UserMixin` objects using `get_id`.
        '''
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal


class User(UserMixin):
    def __init__(self, email=None, password=None, username=None, \
                        userid=None, avatar=None, is_admin=False):
        self.email = email
        self.password = password
        self.username = username
        self.is_admin = is_admin
        self.userid = None
        self.avatar = avatar

    def get_by_id(self, email):
        self.username = 'hh'
        self.email = email
        return self

