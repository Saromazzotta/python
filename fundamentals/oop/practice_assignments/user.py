class User:
    def __init__(self, first_name, last_name, email, age, gold_card_points, is_rewards_member=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.gold_card_points = gold_card_points
        self.is_rewards_member = is_rewards_member

    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points, sep="\n")

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        if self.is_rewards_member == True:
            print("User is already a member.")
            return False
        else: 
            return True
    
    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("User does not have enough points")

saro = User("Saro", "Mazzotta", "Saromazzotta@gmail.com", 25, 200)
firstuser = User("Jeff", "J", "JeffJ@email.com", 20, 200)
seconduser = User("Joe", "H", "JoeH@email.com", 23, 200)
thirduser = User("Billy", "Bob", "Billybob@email.com", 27, 40)


saro.enroll()
saro.display_info()

firstuser.enroll()
firstuser.spend_points(50)
firstuser.display_info()

seconduser.enroll()
seconduser.spend_points(80)
seconduser.display_info()


thirduser.spend_points(50)
thirduser.display_info()
