# Emails_validation-Flask_Mysql-CodingDojo
### Python- Flask - MySQL - Validations
* using flash messages
* RegEx
### Install packages
* ``` pipenv install PyMySQL flask ```
* ``` pipenv shell ```
* ``` python server.py ```
### Regular expression and flash ``` email_model.py ```
```
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

@staticmethod
def validate_email(data):
    is_valid = True
    query = '''
            SELECT * FROM emails WHERE email = %(email)s
            '''
    response_get_email = connectToMySQL('email_db').query_db(query,data)
    if len(response_get_email)>=1:
        print("el mail ya existe")
        flash("el email ya existe")
        is_valid = False
    if not EMAIL_REGEX.match(data['email']):
        print("correo invalido")
        flash("correo invalido")
        is_valid = False

    return  is_valid 

```python
