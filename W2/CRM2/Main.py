#Class
class Client:
    def __init__(self, company_name, email, contract_value):
        self.company_name = company_name
        self.email = email
        self.contract_value = contract_value
    def get_tier(self):
        if self.contract_value > 10000:
            return "VIP"
        else:
            return "Standart"
#Sub class        
class IndividualClient(Client):
    def __init__(self, company_name, email, contract_value, phone):
        super().__init__(company_name, email, contract_value)
        self.phone = phone

#Sub class
class CorporateClient(Client):
    def __init__(self, company_name, email, contract_value, tax_id, representative_name):
        super().__init__(company_name, email, contract_value)
        self.tax_id = tax_id
        self.representative_name = representative_name
    
client1 = IndividualClient("John Doe", "john@email.com", 8000, "123456789")
client2 = CorporateClient("ABC Corp", "contact@abc.com", 20000, "NIP123", "Alice")

print(client1.company_name,":", client1.get_tier()) 
print(client2.company_name,":",client2.get_tier()) 