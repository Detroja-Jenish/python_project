import json
from os import mkdir

class MyDatabase:
    def __readData(self,filePath):
        with open(filePath, 'r') as f:
            a = json.load(f);
        return a;

    def __writeData(self,filePath, data):
        with open(filePath,'w') as f:
            json.dump(data, f, indent=4);

    def __init__(self, user):
        self.__user_directory = "./database/" + user;
        print(self.__user_directory);

    def signUpSetup(self, user_name, password):
        
        users = self.__readData(self.__user_directory + "users.json");
        users[user_name] = password;
        self.__writeData(self.__user_directory + "users.json", users);
        
        mkdir("./database/" + user_name.upper() ) ;
        mkdir("./database/" + user_name.upper() + "/customers") ;

        self.__user_directory = "./database/" + user_name.upper();

        self.__writeData(self.__user_directory + "/customerDetails.json", {});
        
        self.__writeData(self.__user_directory + "/productList.json", {});

        self.addCustomer("Anonymous",{});

    def getOnlyCustomerName(self):
        return self.getAllCustomersDetails().keys();

    def getBills(self):
        allCustomers = self.getOnlyCustomerName();
        
        bill = {}
        
        for customer in allCustomers:
            bill[ customer ] = self.__readData(self.__user_directory + "/customers/" + customer + "/bill_data.json");
            
        return bill;
    
    def updateBillData(self, add_bill, cName):
        
        allDirectories = self.__readData(self.__user_directory + "/customerDetails.json");

        all_bills = self.__readData(allDirectories[ cName ]+"/bill_data.json");

        billNos = all_bills.keys();
        maxBillNo = len(billNos);

        all_bills[maxBillNo] = add_bill;
        self.__writeData(allDirectories[ cName ]+"/bill_data.json", all_bills);

    def getCustomers(self):
        return self.getBills().keys();
    
    def getAllCustomersDetails(self):
        return self.__readData(self.__user_directory + "/customerDetails.json");

    def addCustomer(self, cName, address):
        cNameWithoutSpaces = ("").join(cName.split(" "));
        allCustomers = self.__readData(self.__user_directory + "/customerDetails.json");

        customerDirectory = self.__user_directory + "/customers/" + cNameWithoutSpaces;
        allCustomers[cName] = customerDirectory;
        mkdir(customerDirectory);
        self.__writeData(self.__user_directory + "/customerDetails.json", allCustomers);
        self.__writeData(customerDirectory + "/bill_data.json", {});
        self.__writeData(customerDirectory + "/self_details.json", {"address" : address});

    def getProductList(self):
        return self.__readData(self.__user_directory + "/productList.json");
    
    def addProductList(self, pro):
        try:
            self.__writeData(self.__user_directory + "/productList.json", pro);
        except:
            print("eroor error")
            print(type(pro));
            print(pro);
        


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
