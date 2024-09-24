

# the admin page to make stuff
import os
import sys
import webbrowser



R = '\033[31m' # red 
G = '\033[32m' # green 
Y = '\033[33m' # yellow
C = '\033[36m' # cyan

E = '\033[0m' # end


def conv_bin(txt):
    return ' '.join(format(ord(char), '08b') for char in txt)

while True:
    
    print(f"{R}[1]{E} File to binary \n{G}[2]{E} How to use\n{Y}[3]{E} exit ")
    usr_input = input(f"\n{G}Enter your choice{E} : ")
    
    try:
        usr_input = int(usr_input)
        if not usr_input > 3:
            print(f"selected :{C} {usr_input}{E}")
            
        
    except:
        print(f"{R}only int are allowed !!{E} ")
        sys.exit(68)
        
    
    if usr_input == 1:
        
        file_name = input(f"{Y}Enter filename{E} : ")
        try:
            with open(file_name,'r') as f:
                text = f.read()
                bin = conv_bin(text)
                bin_file = file_name.split('.')[0] + '.bin'
                
                with open(bin_file,'w') as output:
                    output.write(bin)
                    print(f"{bin_file} : {G}successfully saved in {os.getcwd()}/{bin_file} {E}")
                    
        except Exception as e:
            print(e)
            sys.exit(66)

    elif usr_input == 2:
        allow = input("Redirecting to a website[Y/n] : ")
        if allow == "" or allow.lower() == "y":
            webbrowser.open("https://google.com")
            
        else:
            print("abort")
            sys.exit(0)            


    else:
        print("abort")
        sys.exit(2)




                                                                                                        
                                                    
