class Home:
    def new(self, number):
        try:
            int_number = int(number)
            print("Целое число:", int_number)
        except ValueError:
            print("ValueError")
home = Home()
home.new("12")
home.new("1.2")
