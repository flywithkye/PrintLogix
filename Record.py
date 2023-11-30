class Record:
    def __init__(self, id, employee_name, printerModel, color, quantity, paper_size, paper_type, description, date, time, comments):
        self.id = id
        self.employee_name = employee_name
        self.printerModel = printerModel
        self.color = color
        self.quantity = quantity
        self.paper_size = paper_size
        self.paper_type = paper_type
        self.description = description
        self.date = date
        self.time = time
        self.comments = comments
        
    def setId(self, id):
        self.id = id