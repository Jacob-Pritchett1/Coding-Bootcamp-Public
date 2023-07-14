class User:
    def __init__(self, first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self
    def enroll(self):
        if self.is_rewards_member == True:
            print('NOOOOOO. ALREADY A MEMBER')
            return self
        else:
            self.is_rewards_member = True
            print("You are now a rewards member!")
            return self
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        print(f"Your points balance has decreased by: {self.gold_card_points}")
        return self

User_1 = User("Jake", "Pritchett", "MyEmail@Email.com", 900)
User_2 = User("John F", "Kennedy", "360noscopes@headshot.net", 60)
User_3 = User("Howard", "Taft", "Needbiggertubs@bigtub.org", 99)

# print(User_1.first_name)
# print(User_2.email)
# print(User_3.last_name)

# User_1.spend_points(500)
# print(User_1.gold_card_points)


# User_2.enroll()
# print(User_2.is_rewards_member)
# User_2.enroll()

# User_2.spend_points(80)
# print(User_2.gold_card_points)

User_1.display_info().enroll().spend_points(1)
User_2.display_info().enroll().spend_points(2)
User_3.display_info()
