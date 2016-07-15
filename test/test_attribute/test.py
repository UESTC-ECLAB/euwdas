from user import User

user = User().get_by_id('jj')
print user.is_active
