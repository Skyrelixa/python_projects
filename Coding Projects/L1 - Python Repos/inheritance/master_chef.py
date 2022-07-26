from chef import Chef

# enables the master chef to make all the dishes of a regular chef
class MasterChef(Chef):

    # overwriting the special dish function inherited from the regular chef
    def make_special_dish(self):
        print("The chef makes a SUPER special dish.")

    def master_dish(self):
        print("The chef makes a master dish.")