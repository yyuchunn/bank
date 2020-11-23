#HW1
print("第一題")
class Banks():
    def __init__(self, uname):
        self.name = uname
        self.bankname = "Taipei Bank"
        self.__balance = 0
        self.__rate = 30
        self.__service_charge = 0.01
    def save_money(self, money):
        self.__balance = self.__balance + money
        print("存款", money, "完成")
        print(self.name.title(), "帳戶目前餘額: ", self.__balance)
    def withdraw_money(self, money):
        self.__balance = self.__balance - money
        print("提款", money, "完成")
        print(self.name.title(), "帳戶目前餘額: ", self.__balance)
    def ntd_to_usd(self, usd):
        if usd >  self.__balance:
            print("餘額不足")
        else:
            self.result = self.__balance - self.__cal_rate(usd)
            print("將帳戶內新台幣 {} 元換為美金 {} 元".format(self.__cal_rate(usd), usd))
    def __cal_rate(self, usd):
        return round(usd * self.__rate * (1+self.__service_charge), 1)

linbank = Banks("lin")
print("目前開戶銀行: ", linbank.bankname)
linbank.save_money(5000)
linbank.withdraw_money(3000)
linbank.ntd_to_usd(10)

print(" ")

#HW2
print("第二題")
class Geometric():
    def __init__(self):
        self.color = "Green"
class Circle(Geometric):
    def __init__(self, radius):
        self.PI = 3.14159
        self.__radius = radius
        super().__init__()
    @property
    def abc(self):
        return self.__radius
    @abc.setter
    def abc(self, radius):
        self.__radius = radius
    def getDiameter(self):
        return self.__radius * 2
    def getPerimeter(self):
        return self.__radius * 2 * self.PI
    def getArea(self):
        return (self.__radius ** 2) * self.PI
    def getColor(self):
        return self.color

a = Circle(6)
print("半徑={}, 圓周={}, 面積={}".format(a.abc, a.getPerimeter(), a.getArea()))
a.abc = 8
print("修改後的半徑={}, 圓周={} 與面積={}".format(a.abc, a.getPerimeter(), a.getArea()))
