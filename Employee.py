class employee:
    def __init__(self, ID, Name, Salary, Address, Department, Email, Phone):
        self.ID = ID
        self.Name = Name
        self.Salary = Salary
        self.Address = Address
        self.Department = Department
        self.Email = Email
        self.Phone = Phone

    def getID(self):
        return self.ID
    def getName(self):
        return self.Name
    def getSalary(self):
        return self.Salary
    def getAddress(self):
        return self.Address
    def getDepartment(self):
        return self.Department
    def getEmail(self):
        return self.Email
    def getPhone(self):
        return self.Phone
