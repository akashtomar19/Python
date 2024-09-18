from abc import ABC, abstractmethod
from collections import defaultdict

# User class to represent each user
class User:
    def __init__(self, user_id, name, email, mobile):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile = mobile

# ExpenseType Interface
class ExpenseType(ABC):
    @abstractmethod
    def split(self, total_amount, users, user_shares):
        pass

# Equal Split Expense
class EqualExpense(ExpenseType):
    def split(self, total_amount, users, user_shares=None):
        share = round(total_amount / len(users), 2)
        return {user: share for user in users}

# Exact Split Expense
class ExactExpense(ExpenseType):
    def split(self, total_amount, users, user_shares):
        if round(sum(user_shares), 2) != total_amount:
            raise ValueError("The total shares do not add up to the total amount.")
        return {users[i]: user_shares[i] for i in range(len(users))}

# Percent Split Expense
class PercentExpense(ExpenseType):
    def split(self, total_amount, users, user_shares):
        if round(sum(user_shares), 2) != 100:
            raise ValueError("The total percentages do not add up to 100%.")
        return {users[i]: round((user_shares[i] * total_amount) / 100, 2) for i in range(len(users))}

# Expense Factory to create specific expense types
class ExpenseFactory:
    @staticmethod
    def get_expense_type(expense_type):
        if expense_type == "EQUAL":
            return EqualExpense()
        elif expense_type == "EXACT":
            return ExactExpense()
        elif expense_type == "PERCENT":
            return PercentExpense()
        else:
            raise ValueError("Invalid expense type")

# ExpenseManager to handle expenses and balances
class ExpenseManager:
    def __init__(self):
        self.users = {}
        self.balances = defaultdict(lambda: defaultdict(float))

    def add_user(self, user_id, name, email, mobile):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name, email, mobile)
        else:
            raise ValueError(f"User with id {user_id} already exists.")

    def add_expense(self, paid_by, total_amount, users, expense_type, user_shares=None):
        expense = ExpenseFactory.get_expense_type(expense_type)
        splits = expense.split(total_amount, users, user_shares)

        for user, amount in splits.items():
            if user != paid_by:
                self.balances[user][paid_by] += amount
                self.balances[paid_by][user] -= amount

    def show_balances(self):
        printed = False
        for user in self.balances:
            for friend in self.balances[user]:
                if self.balances[user][friend] > 0:
                    print(f"{user} owes {friend}: {round(self.balances[user][friend], 2)}")
                    printed = True
        if not printed:
            print("No balances")

    def show_balance_for_user(self, user_id):
        printed = False
        if user_id not in self.balances:
            print("No balances")
            return

        for friend in self.balances[user_id]:
            if self.balances[user_id][friend] > 0:
                print(f"{user_id} owes {friend}: {round(self.balances[user_id][friend], 2)}")
                printed = True
        for friend in self.balances:
            if self.balances[friend][user_id] > 0:
                print(f"{friend} owes {user_id}: {round(self.balances[friend][user_id], 2)}")
                printed = True
        if not printed:
            print("No balances")

# Main function to demonstrate the usage
if __name__ == "__main__":
    manager = ExpenseManager()

    # Adding users
    manager.add_user("u1", "User1", "user1@example.com", "1234567890")
    manager.add_user("u2", "User2", "user2@example.com", "1234567891")
    manager.add_user("u3", "User3", "user3@example.com", "1234567892")
    manager.add_user("u4", "User4", "user4@example.com", "1234567893")

    # Add expenses
    # Example 1: u1 pays Rs. 1000 split equally among u1, u2, u3, u4
    manager.add_expense("u1", 1000, ["u1", "u2", "u3", "u4"], "EQUAL")

    # Example 2: u1 pays Rs. 1250 for u2 and u3 with exact amounts
    manager.add_expense("u1", 1250, ["u2", "u3"], "EXACT", [370, 880])

    # Example 3: u4 pays Rs. 1200 split by percent among u1, u2, u3, u4
    manager.add_expense("u4", 1200, ["u1", "u2", "u3", "u4"], "PERCENT", [40, 20, 20, 20])

    # Show balances for all
    print("\nBalances for all users:")
    manager.show_balances()

    # Show balance for a specific user
    print("\nBalances for u1:")
    manager.show_balance_for_user("u1")

    print("\nBalances for u4:")
    manager.show_balance_for_user("u4")
