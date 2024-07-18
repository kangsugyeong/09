class Home:
    def __init__(self,where1, size1, what1, price1, year1):
        self.home_where = where1
        self.home_size = size1
        self.home_what = what1
        self.home_price = price1
        self.home_year = year1
    def info(self):
            print(self.home_where + "는 " + self.home_year + "에 지어진 " + self.home_what + "이며 " + self.home_size + ", " + self.home_price + "입니다.")

my_Home = Home("현대아파트","30평", "아파트", "40억", "2018년")
my_Home.info()


class User:
    def __init__(self,name1,age1,num1):
        self.user_name = name1
        self.user_age = age1
        self.user_num = num1

    def info(self):
            print("입력하신 이름은 " + self.user_name + "이며, " + "나이는 " + self.user_age + ", 그리고 연락처는 " + self.user_num + "입니다. ")

my_User = User("수경","25살", "010-0000-0000")
my_User.info()