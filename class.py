# Definindo a classe
class Employee:
    name = "Renan de Moraes"
    # Definindo o método:
    def details(self):
        print("Post: Data Analyst")
        print("Department: Maitenance")
        print("Salary: $1500")

# Create the employee object    
emp = Employee()
# Print the class variable
print("Name:",emp.name)
# Call the class method
emp.details()
