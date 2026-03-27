class ServiceInvoice:
    def __init__(self, rate, hours):
        self.rate = rate
        self.__hours = 0
        self.set_hours(hours)

    def set_hours(self, hours):
        if hours < 0:
            print("Invalid Input")
        else:
            self.__hours = hours
    def calculate_total(self):
        if self.__hours <= 40:
            regular_hours = self.__hours
            overtime_hours = 0
        else:
            regular_hours = 40
            overtime_hours = self.__hours - 40
        base = regular_hours * self.rate
        overtime = overtime_hours * self.rate * 1.5
        total = base + overtime
        return base, overtime, total
    def generate_invoice(self):
        base, overtime, total = self.calculate_total()

        print("=== Invoice ===")
        print(f"Base Pay: {base}")
        print(f"Overtime Bonus: {overtime}")
        print(f"Total: {total}")

invoice1 = ServiceInvoice(10, 50)
invoice1.generate_invoice()

invoice2 = ServiceInvoice(10, 20)
invoice2.generate_invoice()

invoice2 = ServiceInvoice(10, -5)
invoice2.generate_invoice()