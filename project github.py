# to declare a class employee which contains 2 methods: get_detail, forget the name ,employee_id,salary of employee and another method is print details
class employee:
    def get_details(self,n,i,s):
        self.name=n
        self.id=i
        self.sal=s
    def print_details(self):
        return self.name+' '+self.id+' '+self.sal
e1=employee()
e1.get_details('Mohit','01','12346543')
e2=employee()
e2.get_details('Rohit','02','98763')
print(e1.print_details())
print(e2.print_details())
