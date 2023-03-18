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
        #with open(self.__user_directory + "users.json", 'r') as f:
        #    users = json.load(f);
        
        users = self.__readData(self.__user_directory + "users.json");
        users[user_name] = password;
        self.__writeData(self.__user_directory + "users.json", users);
        #with open(self.__user_directory + "users.json", 'w') as f:
        #    json.dump(users, f, indent=4);
        
        mkdir("./database/" + user_name.upper() ) ;
        mkdir("./database/" + user_name.upper() + "/customers") ;

        self.__user_directory = "./database/" + user_name.upper();

        #with open(self.__user_directory + "/bill_data.json", 'w') as f:
        #    json.dump({"Anonymous":[]}, f, indent=4);

        

        #with open(self.__user_directory + "/customerDetails.json", 'w') as f:
        #    json.dump({}, f, indent=4);

        self.__writeData(self.__user_directory + "/customerDetails.json", {});

        #with open(self.__user_directory + "/productList.json", 'w') as f:
        #    json.dump({}, f, indent=4);
        
        self.__writeData(self.__user_directory + "/productList.json", {});

        self.addCustomer("Anonymous",{});

    def getOnlyCustomerName(self):
        return self.getAllCustomersDetails().keys();

    def getBills(self):
        #with open(self.__user_directory + "/bill_data.json" , 'r') as f:
        #    bills = json.load(f);
        return self.__readData(self.__user_directory + "/bill_data.json");
    
    def updateBillData(self, add_bill, cName):
        
        #with open(self.__user_directory + "/customerDetails.json",'r') as f:
        #   allDirectories = json.load(f);
        allDirectories = self.__readData(self.__user_directory + "/customerDetails.json");

        #with open(allDirectories[ cName ]+"/bill_data.json",'r') as f:
        #    all_bills = json.load(f);
        all_bills = self.__readData(allDirectories[ cName ]+"/bill_data.json");

        billNos = all_bills.keys();
        maxBillNo = len(billNos);

        all_bills[maxBillNo] = add_bill;
        #with open(allDirectories[ cName ]+"/bill_data.json",'w') as f:
        #    json.dump(all_bills, f, indent=4);
        self.__writeData(allDirectories[ cName ]+"/bill_data.json", all_bills);

    def getCustomers(self):
        return self.getBills().keys();
    
    def getAllCustomersDetails(self):
        #with open(self.__user_directory + "/customerDetails.json", 'r') as f:
        #    details = json.load(f);
        return self.__readData(self.__user_directory + "/customerDetails.json");

    def addCustomer(self, cName, address):
        cNameWithoutSpaces = ("").join(cName.split(" "));

        #with open(self.__user_directory + "/customerDetails.json", 'r') as f:
        #    allCustomers = json.load(f);
        allCustomers = self.__readData(self.__user_directory + "/customerDetails.json");

        customerDirectory = self.__user_directory + "/customers/" + cNameWithoutSpaces;
        allCustomers[cName] = customerDirectory;
        mkdir(customerDirectory);

        #with open(self.__user_directory + "/customerDetails.json", 'w') as f:
        #    json.dump(allCustomers, f, indent=4);
        self.__writeData(self.__user_directory + "/customerDetails.json", allCustomers);

        #with open(customerDirectory + "/bill_data.json", 'w') as f:
        #    json.dump({},f, indent=4);
        self.__writeData(customerDirectory + "/bill_data.json", {});

        #with open(customerDirectory + "/self_details.json", 'w') as f:
        #    json.dump({"address" : address}, f, indent=4);
        self.__writeData(customerDirectory + "/self_details.json", {"address" : address});

    def getProductList(self):
        #with open(self.__user_directory + "/productList.json", 'r') as f:
        #    a= json.load(f);
        return self.__readData(self.__user_directory + "/productList.json");
    
    def addProductList(self, products):
        try:
            #with open(self.__user_directory + "/productList.json", 'w') as f:
            #    json.dump(products,f, indent=4);
            self.writeData(self.__user_directory + "/productList.json", products);
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
