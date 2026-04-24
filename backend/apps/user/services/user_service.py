class UserService:
    def __init__(self, user):
        self.user = user
    def to_user(self):
        if self.user.is_staff:
            self.user.is_staff = False
            self.user.save()
        return self.user

    def to_admin(self):
        if not self.user.is_staff:
            self.user.is_staff = True
            self.user.save()
        return self.user


# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def save(self):
#         print(f'{self.name} {self.surname} {self.age}')
#
# class UserService:
#     def __init__(self, user):
#         self.user = user
#
#     def block_user(self):
#         self.user.is_staff = True
#         self.user.save()
#
# user = User('Max', 'Ivanov', 25)
# user_ = UserService(user)

# UserService(user).block_user()
# user_.block_user()
#
# class Cinderella:
#     def __init__(self, name, foot_size):
#         self.name = name
#         self.foot_size = foot_size
#         self.has_lost_shoes = False
#
#     def lost_shoes(self):
#         if len(self.name) %2 ==0:
#             self.has_lost_shoes = True
#
#     @classmethod
#     def hello(cls, cinderella):
#         print(f'Hello, my name is {cinderella.name}')
#
#     @staticmethod
#     def hello2(cinderella, inc):
#         cinderella.foot_size += inc
#
#     def hello3(self, inc):
#         self.foot_size += inc
#
#
# cinderella1 = Cinderella('Olenaa', 38)
# cinderella1.hello3(4)
# print(cinderella1.foot_size)
# # Cinderella.hello2(cinderella1, 3)
# print(cinderella1.foot_size)
# Cinderella.hello(cinderella1)
# print(cinderella1.has_lost_shoes)
# cinderella1.lost_shoes()
# print(cinderella1.has_lost_shoes)


# def _send_status_notification(self):
#     """Внутрішній метод для відправки повідомлення"""
#     status_text = "надано" if self.user.is_staff else "скасовано"
#     subject = "Зміна статусу доступу"
#     message = f"Вітаємо, {self.user.username}! Ваш статус персоналу (is_staff) був {status_text}."
#
#     try:
#         send_mail(
#             subject,
#             message,
#             settings.DEFAULT_FROM_EMAIL,
#             [self.user.email],
#             fail_silently=True,
#         )
#         print(f"Повідомлення успішно надіслано на {self.user.email}")
#     except Exception as e:
#         print(f"Помилка відправки пошти: {e}")


