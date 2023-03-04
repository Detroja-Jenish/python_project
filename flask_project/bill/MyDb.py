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

        with open(self.__user_directory + "/productList.json", 'w') as f:
            json.dump({}, f, indent=4);

        self.addCustomer("Anonymous",{});

    def getOnlyCustomerName(self):
        return self.getAllCustomersDetails().keys();

    def getBills(self):
        with open(self.__user_directory + "/bill_data.json" , 'r') as f:
            bills = json.load(f);
        return bills;
    
    def updateBillData(self, add_bill, cName):
        cNameWithoutSpaces = ("").join(cName.split(" "));
        customerDirectory = self.__user_directory + "/" + cNameWithoutSpaces;
        with open(customerDirectory + "/bill_data.json", 'r') as f:
            all_bills = json.load(f);

        billNos = all_bills.keys();
        maxBillNo = len(billNos);

        all_bills[maxBillNo] = add_bill;
        with open(customerDirectory + "/bill_data.json", 'w') as f:
            json.dump(all_bills, f, indent=4);

    def getCustomers(self):
        return self.getBills().keys();
    
    def getAllCustomersDetails(self):
        with open(self.__user_directory + "/customerDetails.json", 'r') as f:
            details = json.load(f);
        return details;

    def addCustomer(self, cName, address):
        cNameWithoutSpaces = ("").join(cName.split(" "));
        customerDirectory = self.__user_directory + "/" + cNameWithoutSpaces;
        mkdir(customerDirectory);
        with open(customerDirectory + "/bill_data.json", 'w') as f:
            json.dump({},f, indent=4);

        with open(customerDirectory + "/self_details.json", 'w') as f:
            json.dump({"address" : address}, f, indent=4);

        with open(self.__user_directory + "/customerDetails.json", 'r') as f:
             allCustomer = json.load(f);

        allCustomer[cName] = "";
        with open(self.__user_directory + "/customerDetails.json", 'w') as f:
            json.dump(allCustomer, f, indent=4);

    def getProductList(self):
        with open(self.__user_directory + "/productList.json", 'r') as f:
            a= json.load(f);
        return a;
    
    def addProductList(self, products):
        try:
            with open(self.__user_directory + "/productList.json", 'w') as f:
                json.dump(products,f, indent=4);
        except:
            print(type(products));
            print(products);
        


#----------------------------------previous tries----------------------------------

#    def updateBillData(self, add_bill, customerName):
#        all_bills = self.getBills();
#        all_bills[ customerName ].append( add_bill );
#        with open(self.__user_directory + "/bill_data.json", 'w') as f:
#            json.dump(all_bills, f, indent=4);
#            print("file saved");
#
#    def addCustomer(self, cName, address):
#        all_customers = self.getAllCustomersDetails();
#        all_customers[ cName ] = address;
#        with open(self.__user_directory + "/customerDetails.json", 'w') as f:
#            json.dump(all_customers, f, indent=4);
#
#        bills = self.getBills();
#        bills[ cName ] = [];
#        with open(self.__user_directory + "/bill_data.json", 'w') as f:
#            json.dump(bills, f, indent=4);
