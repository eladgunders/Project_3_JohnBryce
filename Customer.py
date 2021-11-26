class Customer:

    def __init__(self, id_, fname, lname, address, mobile):
        self.id_ = id_
        self.fname = fname
        self.lname = lname
        self.address = address
        self.mobile = mobile

    def __repr__(self):
        return f'Customer(id_={self.id_}, fname="{self.fname}", lname="{self.lname}",' \
               f' address="{self.address}", mobile="{self.mobile}")'

    def __str__(self):
        return f'Customer[id_={self.id_}, fname="{self.fname}", lname="{self.lname}",' \
               f' address="{self.address}", mobile="{self.mobile}"]'
