class Home:
    def new(self, number):
        try:
            int_number = int(number)
            print("Целое число:", int_number)
        except ValueError:
            print("ValueError")
home_instance = Home()
home_instance.new("12")
home_instance.new("1.2")
