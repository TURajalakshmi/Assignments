class Functions():
    def SubfieldsInAI():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==1):
            print("52452 is odd number")
        else:
            print("52452 is Even number")

    def ElegiblityForMarriage():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age>=21):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    def FindPercent():
        Sub1=int(input("Subject1="))
        Sub2=int(input("Subject2="))
        Sub3=int(input("Subject3="))
        Sub4=int(input("Subject4="))
        Sub5=int(input("Subject5="))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        Percentage=Total/500*100
        print("Total :",Total)
        print("Percentage :",Percentage)
        
    def triangle():
        H=int(input("Height:"))
        B=int(input("Breadth:"))
        Print=input("Area formula:")
        AoT=H*B/2
        print("Area of Triangle:",AoT)
        H1=int(input("Height1:"))
        H2=int(input("Height2:"))
        B=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        poT=H1+H2+B
        print("Perimeter of Triangle:",poT)