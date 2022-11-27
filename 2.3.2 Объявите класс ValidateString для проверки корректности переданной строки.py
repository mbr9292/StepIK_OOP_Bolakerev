class ValidateString:
    def __init__(self, min_length=0, max_length=0):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        if type(string) == str and (self.min_length <= len(string) <= self.max_length):
            return True
        else:
            return False


class StringValue:
    def __init__(self, validator):
        self.validate = validator.validate

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value) == True:
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(validator=ValidateString(3, 100))
    password = StringValue(validator=ValidateString(3, 100))
    email = StringValue(validator=ValidateString(3, 100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'''
            <form>
            Логин: <{self.login}>
            Пароль: <{self.password}>
            Email: <{self.email}>
            </form>
            ''')


# form = RegisterForm('л', 'пароль', 'email')
assert hasattr(ValidateString, 'validate'), "в классе ValidateString отсутствует метод validate"

r = RegisterForm('11111', '1111111', '11111111')
assert hasattr(r, 'login') and hasattr(r, 'password') and hasattr(r,
                                                                  'email'), "в классе RegisterForm должны быть дескрипторы login, password, email"

assert hasattr(RegisterForm, 'show'), "в классе RegisterForm отсутствует метод show"

StringValue.__doc__

frm = RegisterForm("123", "2345", "sc_lib@list.ru")
assert frm.get_fields() == ["123", "2345", "sc_lib@list.ru"], "метод get_fields вернул неверные данные"

frm.login = "root"
assert frm.login == "root", "дескриптор login вернул неверные данные"

v = ValidateString(5, 10)
assert v.validate("hello"), "метод validate вернул неверное значение"
assert v.validate("hell") == False, "метод validate вернул неверное значение"
assert v.validate("hello world!") == False, "метод validate вернул неверное значение"


class A:
    st = StringValue(validator=ValidateString(3, 10))


a = A()
a.st = "hello"

assert a.st == "hello", "дескриптор StringValue вернул неверное значение"
a.st = "d"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной меньше min_length"
a.st = "dапарпаропропропропр"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной больше max_length"
a.st = "dапарпароп"
assert a.st == "dапарпароп", "дескриптор StringValue сохранил строку длиной больше max_length"
