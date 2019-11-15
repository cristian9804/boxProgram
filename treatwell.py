
def boxDraw(h,w):
    if(isinstance(h, int) and isinstance(w, int)): #Here we make sure that the method only accepts integers
        if(h<2 or w<2): # Here we make sure that the right input is entered
            print("Please enter a number greater than 2")
            return
    
        i=1
        while i<=h: #In this first while loop we deal with each row 
            print("\n")
            i+=1
            j=1
            
            while j<=w: #In this second while loop we deal with each column
                
                if(j==1 and i==2): #This makes sure that the top-left of the box is printed
                    print('┌ ',end="")


                elif (j==1 and i-1==h): #This makes sure that the bottm-left of the box is printed
                    print('└ ',end="")


                elif (j==w and i==2): #This makes sure that the top-right of the box is printed
                    print('┐',end="")


                elif (j==1 and i!=0 ): #This makes sure that the Vertical Edges of the box is printed
                    print("| ",end="")


                elif (j==w and i-1==h): #This makes sure that the bottom-right of the box is printed
                    print('┘',end="")


                elif (j==w and i!=0 ): #This statements ensures that the right amount of spacing is added in the "middle" of the box
                    for x in range (2,w):
                        print('   ',end="")
                    print('|',end="")


                elif (j>=2 and i==2): #This prints the horizontal edges at the top of the box
                    print(" - ",end="")


                elif (j>=2 and i-1==h): #This prints the horizontal edges at the bottom of the box
                    print(" - ",end="")

                j+=1
        print("\n")
    else : 
        print("Please enter an Integer")
        return    




boxDraw(6,6)

