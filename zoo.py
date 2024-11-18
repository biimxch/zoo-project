class Zoo:
    def get_ticket_price(self, age):
        # ตรวจสอบกรณีอายุที่ไม่ถูกต้อง
        if age < 0:
            raise ValueError("Age cannot be negative")

        # ตรวจสอบช่วงอายุและคืนราคาตั๋วที่เหมาะสม
        if 0 <= age <= 12:
            return 50
        elif 13 <= age <= 20:
            return 100
        elif 21 <= age <= 60:
            return 150
        elif age > 60:
            return 100
