get_user_password_sql = '''
select
    username, password, usertype
from
    auto_post_users
where
    username = '{username}' and deleted = 0
'''

insert_user_sql = '''
insert into
    auto_post_users
    (`username`, `password`, `usertype`, `name`)
values
    ('{username}', '{password}', {usertype}, '{name}')
'''

update_user_sql = '''
update
    auto_post_users
set
    password = '{password}', usertype = {usertype},
    name = '{name}'
where
    username = '{username}'
'''

insert_house_info_sql = '''
insert into
    auto_post_house_info
    (`file`, `sheet`, `idx`, `community`, `floor`, `total_floor`,
     `addr`, `area`, `price`, `title`, `house_type`, `store`, `source`)
values
    ('%s', '%s', %s, '%s', %s, %s, '%s', %s, %s, '%s', %s, '%s', %s)
'''

house_search_sql = '''
select
    sheet, idx, community, addr, concat(floor),  -- 这里修改了房源名称为地址
    concat(total_floor), concat(area), concat(price),
    title, concat(house_type)
from
    auto_post_house_info
%s
%s
'''