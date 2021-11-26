import sqlite3
from Customer import Customer


class CustomerDataAccess:
    def __init__(self, db_file_path):
        self.db_file_path = db_file_path
        self.con = sqlite3.connect(db_file_path)
        self.db_cursor = self.con.cursor()

    def print_all_customers(self):
        self.db_cursor.execute("SELECT * FROM customers")
        for x in self.db_cursor:
            print(x)
        pass

    def insert_customer(self, customer):
        if not isinstance(customer, Customer):
            print('Insert failed. The customer parameter is not an instance of the "Customer" class.')
            pass
        else:
            row = []
            self.db_cursor.execute(f'SELECT * FROM customers WHERE ID = {customer.id_}')
            for x in self.db_cursor:
                row.append(x)
            if row:
                print('Insert failed. The customer id already exists in the db.')
                pass
            else:
                self.db_cursor.execute(f'INSERT INTO customers VALUES ({customer.id_}, "{customer.fname}", "{customer.lname}", '
                                       f'"{customer.address}", "{customer.mobile}" )')
                self.con.commit()
                print('Insert Done.')
                pass

    def delete_customer(self, customer_id):
        if type(customer_id) != int:
            print('Delete failed. Customer_id must be integer.')
            pass
        else:
            row = []
            self.db_cursor.execute(f'SELECT * FROM customers WHERE ID = {customer_id}')
            for x in self.db_cursor:
                row.append(x)
            if not row:
                print('Delete failed. Id not exist in the db.')
                return None
            else:
                self.db_cursor.execute(f'DELETE FROM customers WHERE ID = {customer_id}')
                self.con.commit()
                print('Delete Done.')
            return True

    def get_all_customers(self):
        customers_ls = []
        self.db_cursor.execute("SELECT * FROM customers")
        for x in self.db_cursor:
            customers_ls.append(x)
        return customers_ls

    def get_customers_by_id(self, customer_id):
        if type(customer_id) != int:
            print('Function failed. Customer_id must be integer.')
            pass
        else:
            row = []
            self.db_cursor.execute(f'SELECT * FROM customers WHERE ID = {customer_id}')
            for x in self.db_cursor:
                row.append(x)
            if not row:
                print('Function failed. Id not exist in the db.')
                pass
            else:
                return Customer(row[0][0], row[0][1], row[0][2],
                                row[0][3], row[0][4])

    def update_customer(self, customer_id, customer):
        if type(customer_id) != int:
            print('Function failed. Customer_id must be integer.')
            pass
        elif not isinstance(customer, Customer):
            print('Insert failed. The customer parameter is not an instance of the "Customer" class.')
            pass
        else:
            row = []
            self.db_cursor.execute(f'SELECT * FROM customers WHERE ID = {customer_id}')
            for x in self.db_cursor:
                row.append(x)
            if not row:
                print('Function failed. Id not exist in the db.')
                return None
            else:
                self.db_cursor.execute(f'UPDATE customers SET FNAME="{customer.fname}", LNAME="{customer.lname}",'
                                       f' ADDRESS="{customer.address}", MOBILE="{customer.mobile}" WHERE ID = {customer_id}')
                self.con.commit()
                print('Update Done')
                return True

    def __repr__(self):
        return f'CustomerDataAccess(db_file_path="{self.db_file_path}")'

    def __str__(self):
        return f'CustomerDataAccess[db_file_path="{self.db_file_path}"]'
