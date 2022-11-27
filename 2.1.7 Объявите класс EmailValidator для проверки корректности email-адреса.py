import random
import re
import string


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        k = random.randrange(1, 100)
        name = ''.join(random.choices(string.ascii_lowercase + string.digits + "_", k=k))

        email = name + "@gmail.com"
        return email

    @classmethod
    def check_email(cls, email):
        pattern = r"^(?!.*\.\.)([-\w\.]{1,100})+@+(?=.{1,50}$)([-\w\.]{1,})+\.([-\w]{1,})$"
        result = re.findall(pattern, email)
        if re.match(pattern, email) is not None:
            return True
        else:
            return False

    @staticmethod
    def __is_email_str(email):
        if type(email) is str:
            return True
        else:
            return False




# # a = EmailValidator.get_random_email()
# # a = 'es4tj0j6l@gmail.com'
# a = 'es4tj0j6l@1..2.33..e222'
# print(a,EmailValidator.check_email(a) )
assert EmailValidator.check_email("sc_lib@list.ru") == True and EmailValidator.check_email("sc_lib@list_ru") == False and EmailValidator.check_email("sc@lib@list_ru") == False and EmailValidator.check_email("sc.lib@list_ru") == False and EmailValidator.check_email("sclib@list.ru") == True and EmailValidator.check_email("sc.lib@listru") == False and EmailValidator.check_email("sc..lib@list.ru") == False, "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
assert EmailValidator.check_email(m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"
#
