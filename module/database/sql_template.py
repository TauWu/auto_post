get_user_password_sql = '''
select
    username, password, usertype
from
    auto_post_users
where
    username = '{username}' and deleted = 0
'''