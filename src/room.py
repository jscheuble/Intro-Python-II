# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):  # n_to, e_to, s_to, w_to):
        self.name = name
        self.description = description
    # self.n_to = n_to
    # self.e_to = e_to
    # self.s_to = s_to
    # self.w_to = w_to

    def __str__(self):
        return '{self.name}: {self.description}'.format(self=self)
