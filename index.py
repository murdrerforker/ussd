code= int(input('enter your code'))


if code == 419 :
  print("""
      1. Account Info
      2. Data Services
      3. Borrow Airtime
      4. Tariff Plans
      #. exit
    """)
 
  option = input('option>>>')
  if option == '1' :
    print("""
          1. My Number
          2. My Account Balance
          3. Sim Registration
          4. My tariff plans
          #. Exit
    """)
    sub_option = input('Sub-option>>>')
    if sub_option == '1' :
        print("""
              Your number is 08008008008
         """)
        
    elif sub_option == '2':
        print("""
              insufficient Balance
         """)
        
    elif sub_option == '3' :
        print("""
              NIN not linked 
         """)
        
    elif  sub_option == '4' :
        print("""
              Na JagbaJagba Era We Dey
              """)

    elif sub_option == '#' :
        exit()


    elif option == '2'  : 
       print("""
             1. Daily
             2. Weekly
             3. Monthly
             4. Yearly
             #. Exit
        """)
    sub_option = input('Sub-option>>>')
    if sub_option == '1' :
        print("""
              Just One day Pere
         """)
        
    elif sub_option == '2':
        print("""
              7 days
         """)
        
    elif sub_option == '3' :
        print("""
              A whole thiiirty days
         """)
        
    elif  sub_option == '4' :
        print("""
              Dem big Boys plan
              """)

    elif sub_option == '#' :
        exit()

    elif option == '3'  : 
        print("""
             1. Check Eligibity
             2. Contact Support 
             3. Onigbese 
             4. Check Again
             #. Exit
    """)
    sub_option = input('Sub-option>>>')
    if sub_option == '1' :
        print("""
              You Be Onigbese joor
         """)
        
    elif sub_option == '2':
        print("""
              Suport is currently busy
         """)
        
    elif sub_option == '3' :
        print("""
              Pay your debt
         """)
        
    elif  sub_option == '4' :
        print("""
              wetin you wan see again
              """)

    elif sub_option == '#' :
        exit()

    elif option == '4'  : 
       print("""
             1. Jagbajantis
             2. Obidiots
             3. Atikufools
             4. Other-wereys
             #. Exit
        """) 
    sub_option = input('Sub-option>>>')
    if sub_option == '1' :
        print("""
              Haa, Tinubu of all the candidates?
         """)
        
    elif sub_option == '2':
        print("""
              Peter Obi cult followers
         """)
        
    elif sub_option == '3' :
        print("""
              Him Carry you go Dubai?
         """)
        
    elif  sub_option == '4' :
        print("""
              Alaye, Democrazy dey somehow here
              """)

    elif sub_option == '#' :
        exit()


    elif option == '#' :
      exit()


else :
    print('INVALID CODE!!!!, Remember this country na 419')
         


