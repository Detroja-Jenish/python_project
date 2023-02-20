import json
from os import mkdir

class MyDatabase:
    def __init__(self, user):
        self.__user_directory = "./database/" + user;
        print(self.__user_directory);

    def signUpSetup(self, user_name, password):
        with open(self.__user_directory + "users.json", 'r') as f:
            users = json.load(f);
        users[user_name] = password;

        with open(self.__user_directory + "users.json", 'w') as f:
            json.dump(users, f, indent=4);
        
        mkdir("./database/" + user_name.upper() ) ;

        self.__user_directory = "./database/" + user_name.upper();

        with open(self.__user_directory + "/bill_data.json", 'w') as f:
            json.dump({"Anonymous":[]}, f, indent=4);

        with open(self.__user_directory + "/customerDetails.json", 'w') as f:
            json.dump({}, f, indent=4);

    def getOnlyCustomerName(self):
        return self.getAllCustomersDetails().keys();

    def getBills(self):
        with open(self.__user_directory + "/bill_data.json" , 'r') as f:
            bills = json.load(f);
        return bills;
    
    def updateBillData(self, add_bill, customerName):
        all_bills = self.getBills();
        all_bills[ customerName ].append( add_bill );
        with open(self.__user_directory + "/bill_data.json", 'w') as f:
            json.dump(all_bills, f, indent=4);
            print("file saved");

    def getCustomers(self):
        return self.getBills().keys();
    
    def getAllCustomersDetails(self):
        with open(self.__user_directory + "/customerDetails.json", 'r') as f:
            details = json.load(f);
        return details;

    def addCustomer(self, cName, address):
        all_customers = self.getAllCustomersDetails();
        all_customers[ cName ] = address;
        with open(self.__user_directory + "/customerDetails.json", 'w') as f:
            json.dump(all_customers, f, indent=4);

        bills = self.getBills();
        bills[ cName ] = [];
        with open(self.__user_directory + "/bill_data.json", 'w') as f:
            json.dump(bills, f, indent=4);

    def addCustomer(self, cName, address, a):
        cNameWithoutSpaces = ("").join(cName.split(" "));
        customerDirectory = self.__user_directory + "/" + cNameWithoutSpaces;
        mkdir(customerDirectory);
        with open(customerDirectory + "/bill_data.json", 'w') as f:
            json.dump({},f, indent=4);

        with open(customerDirectory + "/self_details.json", 'w') as f:
            json.dump({"address" : address}, f, indent=4);


my = MyDatabase("JENISH")
my.addCustomer("Dave Rakshit", {"hello":5}, 0);
