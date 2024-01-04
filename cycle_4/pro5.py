
def vsum(args):
        """variable length argument sum"""
        sum=0
        for num in args:
                sum=sum+int(num)
        print(sum)
limit=input("Enter the elements (sepreted by comma):").split(",")
arra=[]
for i in limit:
        elem=int(i)
        arra.append(elem)
vsum(arra)
