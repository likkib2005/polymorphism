class Father:
    def sleep(self):
        print("sleeps from 10:00 pm to 5:00 am")
    def eat(self):
        print("eating")

class Son(Father):   # 👈 inheritance
    def sleep(self):
        print("sleeps from 2:00 am to 10:00 am")
        super().sleep()

Rithik = Son()
Rithik.sleep()
