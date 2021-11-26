from Customer import Customer
from CustomerDataAccess import CustomerDataAccess
from PyQt5 import QtWidgets, QtCore
import traceback


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.data_access = CustomerDataAccess('hanuka.db')
        self.setGeometry(QtCore.QRect(400, 400, 500, 400))
        self.setStyleSheet('font-size: 15px;')

        self.setWindowTitle("Customers Data Access")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_form = QtWidgets.QFormLayout()
        self.get_all_label = QtWidgets.QLabel('Get All Customers:')
        self.get_all_customers_button = QtWidgets.QPushButton('Get Data')
        self.get_all_customers_button.clicked.connect(self.print_all_customers)
        self.get_by_id_label = QtWidgets.QLabel('Get Customer by ID:')
        self.id_label = QtWidgets.QLabel('ID:')
        self.id_edit = QtWidgets.QLineEdit()
        self.get_by_id_button = QtWidgets.QPushButton('Get Data')
        self.get_by_id_button.clicked.connect(self.get_by_id)
        self.insert_delete_label = QtWidgets.QLabel('Insert or Update Customer:')
        self.insert_id_label = QtWidgets.QLabel('Customer ID:')
        self.insert_id_edit = QtWidgets.QLineEdit()
        self.insert_fname_label = QtWidgets.QLabel('Customer FNAME:')
        self.insert_fname_edit = QtWidgets.QLineEdit()
        self.insert_lname_label = QtWidgets.QLabel('Customer LNAME:')
        self.insert_lname_edit = QtWidgets.QLineEdit()
        self.insert_address_label = QtWidgets.QLabel('Customer ADDRESS:')
        self.insert_address_edit = QtWidgets.QLineEdit()
        self.insert_mobile_label = QtWidgets.QLabel('Customer MOBILE:')
        self.insert_mobile_edit = QtWidgets.QLineEdit()
        self.insert_customer_button = QtWidgets.QPushButton('Insert Customer')
        self.insert_customer_button.clicked.connect(self.insert_customer_to_db)
        self.delete_customer_label = QtWidgets.QLabel('Delete Customer:')
        self.delete_id_label = QtWidgets.QLabel('Customer ID:')
        self.delete_id_edit = QtWidgets.QLineEdit()
        self.delete_customer_button = QtWidgets.QPushButton('Delete Customer')
        self.delete_customer_button.clicked.connect(self.delete_customer_in_db)
        self.update_customer_button = QtWidgets.QPushButton('Update Customer')
        self.update_customer_button.clicked.connect(self.update_customer_in_db)
        self.main_form.addRow(self.get_all_label)
        self.main_form.addRow(self.get_all_customers_button)
        self.main_form.addRow(self.get_by_id_label)
        self.main_form.addRow(self.id_label, self.id_edit)
        self.main_form.addRow(self.get_by_id_button)
        self.main_form.addRow(self.insert_delete_label)
        self.main_form.addRow(self.insert_id_label, self.insert_id_edit)
        self.main_form.addRow(self.insert_fname_label, self.insert_fname_edit)
        self.main_form.addRow(self.insert_lname_label, self.insert_lname_edit)
        self.main_form.addRow(self.insert_address_label, self.insert_address_edit)
        self.main_form.addRow(self.insert_mobile_label, self.insert_mobile_edit)
        self.main_form.addRow(self.insert_customer_button)
        self.main_form.addRow(self.update_customer_button)
        self.main_form.addRow(self.delete_customer_label)
        self.main_form.addRow(self.delete_id_label, self.delete_id_edit)
        self.main_form.addRow(self.delete_customer_button)
        self.main_layout.addLayout(self.main_form)
        self.data_label = QtWidgets.QLabel('Data: ')
        self.main_layout.addWidget(self.data_label)
        self.data_edit = QtWidgets.QTextEdit()
        self.main_layout.addWidget(self.data_edit)
        self.status_line = QtWidgets.QLabel()
        self.main_layout.addWidget(self.status_line)

    def print_all_customers(self):
        self.data_edit.setText('')
        self.status_line.setText('')
        customers_ls = self.data_access.get_all_customers()
        for customer in customers_ls:
            self.data_edit.append(f'{customer}')

    def get_by_id(self):
        id_ = self.id_edit.text()
        if id_ == '':
            self.status_line.setText('ID must be filled.')
            pass
        else:
            try:
                self.status_line.setText('')
                customer = self.data_access.get_customers_by_id(int(id_))
                self.data_edit.setText('')
                self.data_edit.append(f'{customer}')
            except ValueError:
                self.status_line.setText('ID must be integer.')

    def insert_customer_to_db(self):
        id_ = self.insert_id_edit.text()
        fname = self.insert_fname_edit.text()
        lname = self.insert_lname_edit.text()
        address = self.insert_address_edit.text()
        mobile = self.insert_mobile_edit.text()
        if id_ == '' or fname == '' or lname == '' or address == '' or mobile == '':
            self.status_line.setText('All insert fields must be filled.')
            pass
        elif id_ != '':
            try:
                int_id_ = int(id_)
                inserted_customer = Customer(int_id_, fname, lname, address, mobile)
                customer = self.data_access.get_customers_by_id(int_id_)
                if isinstance(customer, Customer):
                    self.status_line.setText('Insert failed. The customer id already exists in the db.')
                    pass
                else:
                    self.data_access.insert_customer(inserted_customer)
                    self.status_line.setText('Insert Done.')
            except ValueError:
                self.status_line.setText('ID must be integer.')
                pass

    def delete_customer_in_db(self):
        id_ = self.delete_id_edit.text()
        if id_ == '':
            self.status_line.setText('Deleted customer ID must be filled.')
            pass
        elif id_ != '':
            try:
                int_id_ = int(id_)
                output = self.data_access.delete_customer(int_id_)
                if output is None:
                    self.status_line.setText('Delete failed. No such ID in the db.')
                    pass
                else:
                    self.status_line.setText('Delete Done.')
            except ValueError:
                self.status_line.setText('ID must be integer.')
                pass

    def update_customer_in_db(self):
        id_ = self.insert_id_edit.text()
        fname = self.insert_fname_edit.text()
        lname = self.insert_lname_edit.text()
        address = self.insert_address_edit.text()
        mobile = self.insert_mobile_edit.text()
        if id_ == '' or fname == '' or lname == '' or address == '' or mobile == '':
            self.status_line.setText('All insert fields must be filled.')
            pass
        elif id_ != '':
            try:
                int_id_ = int(id_)
                updated_customer = Customer(int_id_, fname, lname, address, mobile)
                customer = self.data_access.get_customers_by_id(int_id_)
                if not isinstance(customer, Customer):
                    self.status_line.setText('Update failed. N0 such ID in the db.')
                    pass
                else:
                    self.data_access.update_customer(int_id_, updated_customer)
                    self.status_line.setText('Update Done.')
            except ValueError:
                self.status_line.setText('ID must be integer.')
                pass


def excepethook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    errorReport("Error catched:\n" + tb)
    print("Error message:\n", tb)
    QtWidgets.QApplication.quit()


def errorReport(string):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(string)
    msg.setWindowTitle("Error")
    msg.exec_()


def messageReport(string):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText(string)
    msg.setWindowTitle("Message")
    msg.exec_()

if __name__ == "__main__":
    import sys

    sys.excepthook = excepethook

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


