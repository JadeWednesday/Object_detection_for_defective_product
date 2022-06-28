#!python

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("content-type: text/html")
print()

import cgi, os

files = os.listdir('data')
print(files)

list_str = ''
for item in files:
    list_str = list_str + '<li> <a href="index.py?id={name}">{name}</a> </li>'.format(name=item)

form = cgi.FieldStorage()
page_id = form.getvalue('id')

if 'id' in form:
    page_id = form.getvalue('id')
    description = open('data/' + page_id, 'r').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(page_id)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="page_id" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(page_id)
else:
    page_id = 'Welcome'
    description = 'Hello, Web'
    update_link = ''
    delete_action = ''

print('홈페이지를 cgi로 구현')
print()
print('''
<!DOCTYPE html>
<html lang="ko" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>WEB1 - Welcome</title>
  </head>
  <body>

    <h1> <a href="index.py">WEB</a> </h1>

    <ol>
      {list_str}
    </ol>

    <a href="create.py">create</a>
    {update_link}
    {delete_action}

    <h2>{title}</h2>

    <p>{description}</p>

  </body>
</html>
'''.format(title=page_id, description=description, list_str=list_str, update_link=update_link, delete_action=delete_action))
