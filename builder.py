
# Builder is often behind-the-scenes in frameworks.


class User:
    """
    Product class representing the final object.

    Key points:
    - Stores the main data (name, age, email, phone, address).
    - Can be created directly or via a Builder.
    - Fields can be optional, allowing flexibility.
    """
    def init(self, name, age, email=None, phone=None, address=None):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address

    def str(self):
        return f"{self.name}, {self.age}, {self.email}, {self.phone}, {self.address}"


class UserBuilder:
    """
    Builder class to construct User objects step-by-step.

    When to use:
    - Object has many optional attributes.
    - Construction needs to be flexible or readable.
    - Multiple variations of object construction are required.

    How it works:
    1. Create a Builder with required parameters.
    2. Set optional attributes via setter methods.
    3. Call build() to get the final User object.
    """
    def init(self, name, age):
        # Required parameters
        self.name = name
        self.age = age
        # Optional parameters initialized to None
        self.email = None
        self.phone = None
        self.address = None

    def set_email(self, email):
        """Set optional email attribute."""
        self.email = email
        return self  # Allow method chaining

    def set_phone(self, phone):
        """Set optional phone attribute."""
        self.phone = phone
        return self

    def set_address(self, address):
        """Set optional address attribute."""
        self.address = address
        return self

    def build(self):
        """Create and return the final User object."""
        return User(self.name, self.age, self.email, self.phone, self.address)


# Example usage (can be from UI, API, or direct code)
user = (UserBuilder("Alice", 30)
        .set_email("alice@example.com")
        .set_phone("123456789")
        .build())

print(user)