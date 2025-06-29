from datetime import datetime

class User:
    # class variable (shared across all instances)
    user_count = 0

    def __init__(self, username):
        self.username = username
        self.created_at = datetime.now()
        User.user_count += 1  # updating class variable

    # instance method — works with instance data
    def display_info(self):
        print(f"trying to display user_count from instance method:{ self.user_count}")
        print(f"User: {self.username}, Created at: {self.created_at}")

    # class method — works with class-level data
    @classmethod
    def get_user_count(cls):
        print(f"Total users created: {cls.user_count}")

    # alternative constructor using class method
    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous")

    # static method — utility, unrelated to instance or class
    @staticmethod
    def validate_username(username):
        if len(username) < 3:
            print("Invalid username: too short")
            return False
        if not username.isalnum():
            print("Invalid username: should be alphanumeric")
            return False
        print("Username is valid")
        return True




# Static method usage — no need for an instance
User.validate_username("ab")          # Invalid username: too short
User.validate_username("ashwani123")  # Username is valid

# Create users
u1 = User("ashwani")
u2 = User.create_anonymous()          # alternative constructor

# Instance methods
u1.display_info()
u2.display_info()

# Class method
User.get_user_count()                 # Total users created: 2




#  What if you change user_count in an instance?

u1.user_count = 999
print(User.user_count)  # Still correct: 2
print(u1.user_count)    # 999 (shadowed at instance level)