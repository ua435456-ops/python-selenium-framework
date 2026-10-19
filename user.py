class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_login_info(self):
        return f"Логин: {self.name}, Пароль: {self.password}"

    def change_password(self, new_password):
        self.password = new_password
        print(f"Пароль для {self.name} изменен")


user1 = User("standart_user", "secret_sauce")
user2 = User("locked_out_user", "secret_sauce")

print(user1.get_login_info())
print(user2.get_login_info())

user1.change_password("new_secret_123")
print(user1.get_login_info())