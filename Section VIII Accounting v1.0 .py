import tkinter
from tkinter import *
from tkinter import messagebox
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def calculation():

    import matplotlib
    import matplotlib.pyplot as plt
    import sqlite3

    #connectionObject = sqlite3.connect("Finance.db")
    #cursorObject = connectionObject.cursor()

    subscriptionR = entry_1.get()
    int_subscriptionR = int(subscriptionR)
    
    entrance_fee = entry_2.get()
    int_entrance_fee = int(entrance_fee)
    
    life_membership_fee = entry_3.get()
    int_life_membership_fee = int(life_membership_fee)
    
    general_donation = entry_4.get()
    int_general_donation = int(general_donation)
    
    locker_rent = entry_5.get()
    int_locker_rent = int(locker_rent)
    
    legacy = entry_6.get()
    int_legacy = int(legacy)
    
    proc_charityShow = entry_7.get()
    int_proc_charityShow = int(proc_charityShow)
    
    sale_of_furniture = entry_8.get()
    int_sale_of_furniture = int(sale_of_furniture)
    
    sale_of_buiding = entry_9.get()
    int_sale_of_buiding = int(sale_of_buiding)
    
    sale_of_periodicals = entry_10.get()
    int_sale_of_periodicals = int(sale_of_periodicals)
    
    donation_sportsfund = entry_11.get()
    int_donation_sportsfund = int(donation_sportsfund)
    
    donation_tournamentfund = entry_12.get()
    int_donation_tournamentfund = int(donation_tournamentfund)
    
    misc_recipts = entry_13.get()
    int_misc_recipts = int(misc_recipts)
    
    

    # Payment Values

    honarium = entry_14.get()
    int_honarium = int(honarium)
    
    audit_fee = entry_15.get()
    int_audit_fee = int(audit_fee)
    
    wages_salaries = entry_16.get()
    int_wages_salaries = int(wages_salaries)
    
    repair_renewals = entry_17.get()
    int_repair_renewals = int(repair_renewals)
    
    telephone_charges = entry_18.get()
    int_telephone_charges = int(telephone_charges)
    
    advertisement = entry_19.get()
    int_advertisement = int(advertisement)
    
    postage_courier = entry_20.get()
    int_postage_courier = int(postage_courier)
    
    rent = entry_21.get()
    int_rent = int(rent)
    
    insurance = entry_22.get()
    int_insurance = int(insurance)
    
    rates_taxes = entry_23.get()
    int_rates_taxes = int(rates_taxes)
    
    purchase_furniture = entry_24.get()
    int_purchase_furniture = int(purchase_furniture)
    
    purchase_books = entry_25.get()
    int_purchase_books = int(purchase_books)
    
    purchase_building = entry_26.get()
    int_purchase_building = int(purchase_building)
    
    entertainment = entry_27.get()
    int_entertainment  = int(entertainment)
    
    petty_expences = entry_28.get()
    int_petty_expences = int(petty_expences)

    #opening balances

    capital_fund = entry_29.get()
    int_capital_fund = int(capital_fund)
    
    cash_in_handOP = entry_30.get()
    int_cash_in_handOP = int(cash_in_handOP)
    
    cash_at_bankOP = entry_31.get()
    int_cash_at_bankOP = int(cash_at_bankOP)
    
    furnitureOP = entry_32.get()
    int_furnitureOP = int(furnitureOP)
    
    buildingOP = entry_33.get()
    int_buildingOP = int(buildingOP)
    
    booksOP = entry_34.get()
    int_booksOP = int(booksOP)
    
    sports_fundOP = entry_35.get()
    int_sports_fundOP = int(sports_fundOP)
    
    os_subscriptionOP = entry_36.get()
    int_os_subscriptionOP = int(os_subscriptionOP)
    
    adv_subscriptionOP = entry_37.get()
    int_adv_subscriptionOP = int(adv_subscriptionOP)
    
    staionary_postageOP = entry_38.get()
    int_staionary_postageOP = int(staionary_postageOP)
    
    tournament_fundOP = entry_39.get()
    int_tournament_fundOP = int(tournament_fundOP)
    
    stock_of_medicinesOP = entry_40.get()
    int_stock_of_medicinesOP = int(stock_of_medicinesOP)

    #Addon

    dep_on_building = entry_41.get()
    int_dep_on_building = int(dep_on_building)
    
    dep_on_furniture = entry_42.get()
    int_dep_on_furniture = int(dep_on_furniture)
    
    writtenoff_books = entry_43.get()
    int_writtenoff_books = int(writtenoff_books)
    
    os_subscription = entry_44.get()
    int_os_subscription = int(os_subscription)
    
    adv_subscription = entry_45.get()
    int_adv_subscription = int(adv_subscription)
    
    cash_in_handADD = entry_46.get()
    int_cash_in_handADD = int(cash_in_handADD)
    
    cash_at_bankADD = entry_47.get()
    int_cash_at_bankADD = int(cash_at_bankADD)
    
    drover_sports_fund = entry_48.get()
    int_drover_sports_fund = int(drover_sports_fund)
    
    drover_tournament_fund = entry_49.get()
    int_drover_tournament_fund = int(drover_tournament_fund)
    
    osWages_salaries = entry_50.get()
    int_osWages_salaries = int(osWages_salaries)
    
    advWages_salaries = entry_51.get()
    int_advWages_salaries = int(advWages_salaries)
    
    stationary_postageCL = entry_52.get()
    int_stationary_postageCL = int(stationary_postageCL)

    #Calucation of adjustment
    
    if int_sale_of_furniture > 0:
        furnitureADJ_1 = ((int_furnitureOP+int_purchase_furniture))-(int_sale_of_furniture)
        furnitureADJ = ((furnitureADJ_1))-(furnitureADJ_1)*int_dep_on_furniture/100
    else:
        furnitureADJ = (int_furnitureOP+int_purchase_furniture)-(int_furnitureOP+int_purchase_furniture)*int_dep_on_furniture/100


    if int_sale_of_buiding > 0:
        buildingADJ_1 = ((int_buildingOP+int_purchase_building))-(int_sale_of_buiding)
        buildingADJ = ((buildingADJ_1))-(buildingADJ_1)*int_dep_on_building/100

    else:
        buildingADJ = (int_buildingOP+int_purchase_building)-(int_buildingOP+int_purchase_building)*int_dep_on_building/100
    
    stationaryConsumptionADJ = (int_staionary_postageOP+int_postage_courier) - int_stationary_postageCL
    booksADJ = ((int_booksOP+ int_purchase_books)) - int_writtenoff_books
    wages_salaryADJ =  (int_wages_salaries+int_osWages_salaries)-int_advWages_salaries
    tournamentfundADJ = (int_donation_tournamentfund+int_tournament_fundOP)- int_drover_tournament_fund
    sportsfundADJ = (int_donation_sportsfund+int_sports_fundOP) - int_drover_sports_fund
    subscriptionADJ = (int_subscriptionR+int_os_subscription+int_adv_subscriptionOP)-int_adv_subscription

    #Calculation of I&E account

    expences = stationaryConsumptionADJ+int_honarium+int_audit_fee+wages_salaryADJ+int_telephone_charges+int_advertisement+int_rent+int_insurance+int_rates_taxes+int_entertainment+int_petty_expences+(int_buildingOP+int_purchase_building)*int_dep_on_building/100+(int_buildingOP+int_purchase_building)*int_dep_on_building/100
    income = int_entrance_fee+int_general_donation+int_locker_rent+int_legacy+int_proc_charityShow+int_misc_recipts+subscriptionADJ

    
    if income > expences:
        total_of_INE = income
    else:
        total_of_INE = expences


    INE_balance = income-expences

    INE_def = 0
    INE_surp = 0

    if INE_balance > 0:
        INE_result = "Surplus"
    else:
        INE_result = "Deficiet"

    
    #Calculation of capital fund (if not given)

    capital_fundADJ = 0
    
    if int_capital_fund == 0:
        capital_fundADJ = (cash_in_handOP +cash_at_bankOP+furnitureOP+buildingOP+booksOP+os_subscriptionOP+staionary_postageOP+stock_of_medicinesOP)- (sports_fundOP+adv_subscriptionOP+tournament_fundOP)

    #calculation of asset
    asset = int_cash_in_handADD+int_cash_at_bankADD+booksADJ+furnitureADJ+buildingADJ+int_advWages_salaries+int_os_subscription+int_stock_of_medicinesOP
    #calculation of liability
    liability = int_capital_fund+capital_fundADJ+INE_balance+int_life_membership_fee+int_adv_subscription+tournamentfundADJ+sportsfundADJ+wages_salaryADJ+int_osWages_salaries

    assetADJ = 0
    liabilityADJ = 0

    if liability < asset:
        liabilityadj = asset - liability
    elif liability > asset:
        assetADJ = liability - asset
        
    #missingfigure since npo deals with insufficent data 
    asset = asset + assetADJ 
    liability = liability + liabilityADJ

    connectionObject = sqlite3.connect("Finance.db")
    cursorObject = connectionObject.cursor()
    year = 2019
    cursorObject.execute('''CREATE TABLE if not exists finance (
            Year INTEGER PRIMARY KEY,
            Expense INTEGER,
            Income INTEGER,
            Surplus  INTEGER,
            Deficit INTEGER,
            IE_total INTEGER,
            Stationary_consumed INTEGER,
            Furniture_balance INTEGER,
            Building_balance INTEGER,
            Sports_fund_balance INTEGER,
            Tournament_fund_balance INTEGER,
            Asset INTEGER,
            Liability INTEGER)''')
    surp = 0
    deficit = 0

    cursorObject.execute('''INSERT INTO finance values(?,?,?,?,?,?,?,?,?,?,?,?,?)''', (
        year, expences, income, INE_surp, INE_def, total_of_INE, stationaryConsumptionADJ, furnitureADJ, buildingADJ,
        sportsfundADJ, tournamentfundADJ, asset, liability))

    # (Year,Expense,Income,Surplus,Deficit,IE_total,Stationary_consumed,Furniture_balance,Building_balance,Sports_fund_balance,Tournament_fund_balance,Asset,Liability)

    #rows = cursorObject.fetchall()

    connectionObject.commit()
    connectionObject.close()


    

    root = Tk()
    root.title("Report")
    root.geometry('1129x575')
    
    label_1 = Label(root,font=("helvetica", 22, "bold"), text="Section VIII Financial Report")
    label_1.grid(columnspan=4,padx=30,pady=30)

    label_2 = Label(root,font =("courier",12, "bold" ),text="Expences of the Organisation : ")
    label_2.grid(row=4, column=1, padx=10,pady=10)
    label_3 = Label(root, text=expences)
    label_3.grid(row=4, column=2)

    label_4 = Label(root, font =("courier",12, "bold" ),text="Income of the Organisation : ")
    label_4.grid(row=5,  column=1, padx=10,pady=10)
    label_5 = Label(root, text=income)
    label_5.grid(row=5, column=2)

    label_6 = Label(root,font =("courier",12, "bold" ), text=INE_result)
    label_6.grid(row=6,  column=1, padx=10,pady=10)
    label_7 = Label(root, text=INE_balance)
    label_7.grid(row=6, column=2)

    label_8 = Label(root, font =("courier",12, "bold" ),text="Income & Expenditure account Total: ")
    label_8.grid(row=7,  column=1, padx=10,pady=10)
    label_9 = Label(root, text=total_of_INE)
    label_9.grid(row=7, column=2)

    label_10 = Label(root,font =("courier",12, "bold" ), text="Stationary Consumed: ")
    label_10.grid(row=8,  column=1, padx=10,pady=10)
    label_11 = Label(root, text=stationaryConsumptionADJ)
    label_11.grid(row=8, column=2)

    label_12 = Label(root, font =("courier",12, "bold" ),text="Current year Furniture left overs: ")
    label_12.grid(row=9,  column=1, padx=10,pady=10)
    label_13 = Label(root, text=furnitureADJ)
    label_13.grid(row=9, column=2)

    label_14 = Label(root, font =("courier",12, "bold" ),text="Current year Building left overs: ")
    label_14.grid(row=10,  column=1, padx=10,pady=10)
    label_15 = Label(root, text=buildingADJ)
    label_15.grid(row=10, column=2)

    label_16 = Label(root,font =("courier",12, "bold" ), text="Sports fund Balance: ")
    label_16.grid(row=11,  column=1, padx=10,pady=10)
    label_17 = Label(root, text=sportsfundADJ)
    label_17.grid(row=11, column=2)

    label_18 = Label(root, font =("courier",12, "bold" ),text="Tournament fund Balance: ")
    label_18.grid(row=12,  column=1, padx=10,pady=10)
    label_19 = Label(root, text=tournamentfundADJ)
    label_19.grid(row=12, column=2)

    label_18 = Label(root, font =("courier",12, "bold" ),text="Assets: ")
    label_18.grid(row=13,  column=1, padx=10,pady=10)
    label_19 = Label(root, text=asset)
    label_19.grid(row=13, column=2)

    label_18 = Label(root, font =("courier",12, "bold" ),text="Liability: ")
    label_18.grid(row=14,  column=1, padx=10,pady=10)
    label_19 = Label(root, text=liability)
    label_19.grid(row=14, column=2)



    #connectionObject.close()

    figure1 = plt.Figure(figsize=(6.5, 5), dpi=105)
    ax1 = figure1.add_subplot(122)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().place(x=450, y=50)

    if INE_balance > 0:

        labels = ('Income', 'Expenditure', 'Surplus')
        sizes = [income, expences, INE_balance]
        explode = (0, 0, 0.1)
        # fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # plt.show()

    else:
        ax1 = figure1.add_subplot(122)
        labels = ('Income', 'Expenditure', 'Deficit')
        sizes = [income, expences, abs(INE_balance)]
        explode = (0, 0, 0.1)
        # fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    #print("Expences",expences)
    #print("Income",income)
    #print("INE Result",INE_result ,INE_balance)
    #print("INE Total",total_of_INE)

    #print('asset',asset)
    #print('liability',liability)

    
root = Tk()
root.title("Preparation Of Section VIII Financial Statement")
root.geometry('1800x1800')

label_1 = Label(root,font=("helvetica", 22, "bold"), text="Data For Section VIII FS  :")
label_1.grid(columnspan=4,padx=30,pady=30)

     
label_2 = Label(root,font =("courier",18, "bold" ),text="Reciepts")
label_2.grid(row=1, column=2)

label_3 = Label(root, text="Subscription ")
label_3.grid(row=4, sticky=E, column=1, padx=10,pady=10)
entry_1 = Entry(root, width=15)
entry_1.grid(row=4, column=2)

label_4 = Label(root, text="Entrance fees ")
label_4.grid(row=5, sticky=E, column=1, padx=10,pady=10)
entry_2 = Entry(root, width=15)
entry_2.grid(row=5, column=2)

label_5 = Label(root, text="Life membership fees ")
label_5.grid(row=6, sticky=E, column=1, padx=10,pady=10)
entry_3 = Entry(root, width=15)
entry_3.grid(row=6, column=2)

label_6 = Label(root, text="General Donation ")
label_6.grid(row=7, sticky=E, column=1, padx=10,pady=10)
entry_4 = Entry(root, width=15)
entry_4.grid(row=7, column=2)

label_7 = Label(root, text="Locker Rent ")
label_7.grid(row=8, sticky=E, column=1, padx=10,pady=10)
entry_5 = Entry(root, width=15)
entry_5.grid(row=8, column=2)

label_8 = Label(root, text="legacy ")
label_8.grid(row=9, sticky=E, column=1, padx=10,pady=10)
entry_6 = Entry(root, width=15)
entry_6.grid(row=9, column=2)


label_9 = Label(root, text="Proceeds from charity show")
label_9.grid(row=10, sticky=E, column=1, padx=10,pady=10)
entry_7 = Entry(root, width=15)
entry_7.grid(row=10, column=2)

label_10 = Label(root,text="Sale of Furniture ")
label_10.grid(row=11,sticky = E, column=1, padx=10,pady=10)
entry_8 = Entry(root, width=15)
entry_8.grid(row=11, column=2)
    
label_11 = Label(root,text="Sale of Building ")
label_11.grid(row=12,sticky = E, column=1, padx=10,pady=10)
entry_9 = Entry(root, width=15)
entry_9.grid(row=12, column=2)

label_12 = Label(root,text="Sale of Periodicals")
label_12.grid(row=13,sticky = E, column=1, padx=10,pady=10)
entry_10 = Entry(root, width=15)
entry_10.grid(row=13, column=2)

label_13 = Label(root,text="Donation on Sports fund")
label_13.grid(row=14,sticky = E, column=1, padx=10,pady=10)
entry_11 = Entry(root, width=15)
entry_11.grid(row=14, column=2)

label_14 = Label(root,text="Donation on Tournament fund")
label_14.grid(row=15,sticky = E, column=1, padx=10,pady=10)
entry_12 = Entry(root, width=15)
entry_12.grid(row=15, column=2)

label_15 = Label(root,text="Miscellaneance Recipts")
label_15.grid(row=16,sticky = E, column=1, padx=10,pady=10)
entry_13 = Entry(root, width=15)
entry_13.grid(row=16, column=2)


    

label_16 = Label(root, font = ("courier",18,"bold"),text="Payments")
label_16.grid(row=1, column= 5)

Label_17 = Label(root, text="Honararium ")
Label_17.grid(row=4, sticky=E, column=4)
entry_14 = Entry(root, width=15)
entry_14.grid(row=4, column=5)

label_18 = Label(root, text="Audit Fee ")
label_18.grid(row=5, sticky=E, column=4)
entry_15 = Entry(root, width=15)
entry_15.grid(row=5, column=5)

label_19 = Label(root, text="Wages & salaries ")
label_19.grid(row=6, sticky=E, column=4)
entry_16 = Entry(root, width=15)
entry_16.grid(row=6, column=5)

label_20 = Label(root, text="Repair & Renewals ")
label_20.grid(row=7, sticky=E, column=4)
entry_17 = Entry(root, width=15)
entry_17.grid(row=7, column=5)

label_21 = Label(root, text="Telephone Charges ")
label_21.grid(row=8, sticky=E, column=4)
entry_18 = Entry(root, width=15)
entry_18.grid(row=8, column=5)

label_22 = Label(root, text="Advertisement ")
label_22.grid(row=9, sticky=E, column=4)
entry_19 = Entry(root, width=15)
entry_19.grid(row=9, column=5)

label_23 = Label(root, text="Postage and Courier ")
label_23.grid(row=10, sticky=E, column=4)
entry_20 = Entry(root, width=15)
entry_20.grid(row=10, column=5)

label_24 = Label(root, text="Rent ")
label_24.grid(row=11, sticky=E, column=4)
entry_21 = Entry(root, width=15)
entry_21.grid(row=11, column=5)

label_25 = Label(root, text="Insurance ")
label_25.grid(row=12, sticky=E, column=4)
entry_22 = Entry(root, width=15)
entry_22.grid(row=12, column=5)

label_26 = Label(root, text="Rates & Taxes ")
label_26.grid(row=13, sticky=E, column=4)
entry_23 = Entry(root, width=15)
entry_23.grid(row=13, column=5)

label_27 = Label(root, text="Purchase of Furniture")
label_27.grid(row=14, sticky=E, column=4)
entry_24 = Entry(root, width=15)
entry_24.grid(row=14, column=5)

label_28 = Label(root, text="Purchase of Books")
label_28.grid(row=15, sticky=E, column=4)
entry_25 = Entry(root, width=15)
entry_25.grid(row=15, column=5)

label_29 = Label(root, text="Purchase of Building")
label_29.grid(row=16, sticky=E, column=4)
entry_26 = Entry(root, width=15)
entry_26.grid(row=16, column=5)

label_30 = Label(root, text="Entertainment Expences")
label_30.grid(row=17, sticky=E, column=4)
entry_27 = Entry(root, width=15)
entry_27.grid(row=17, column=5)

label_31 = Label(root, text="Petty Expences")
label_31.grid(row=18, sticky=E, column=4, padx=10,pady=10)
entry_28 = Entry(root, width=15)
entry_28.grid(row=18, column=5)



label_32 = Label(root,font = ("courier",18,"bold"),text="Opening Balances")
label_32.grid(row=1, column= 7)

label_33 = Label(root, text="Capital Fund ")
label_33.grid(row=4, sticky=E, column=6)
entry_29 = Entry(root, width=15)
entry_29.grid(row=4, column=7)

label_34 = Label(root, text="Cash in hand ")
label_34.grid(row=5, sticky=E, column=6)
entry_30 = Entry(root, width=15)
entry_30.grid(row=5, column=7)

label_35= Label(root, text="Cash at bank ")
label_35.grid(row=6, sticky=E, column=6)
entry_31= Entry(root, width=15)
entry_31.grid(row=6, column=7)

label_36= Label(root, text="Furniture ")
label_36.grid(row=7, sticky=E, column=6)
entry_32 = Entry(root, width=15)
entry_32.grid(row=7, column=7)

label_37= Label(root, text="Building")
label_37.grid(row=8, sticky=E, column=6)
entry_33 = Entry(root, width=15)
entry_33.grid(row=8, column=7)

label_38 = Label(root, text="Books ")
label_38.grid(row=9, sticky=E, column=6)
entry_34 = Entry(root, width=15)
entry_34.grid(row=9, column=7)

label_39 = Label(root, text="Sports fund")
label_39.grid(row=10, sticky=E, column=6)
entry_35 = Entry(root, width=15)
entry_35.grid(row=10, column=7)

label_40= Label(root, text="Outstanding Subscription ")
label_40.grid(row=11, sticky=E, column=6)
entry_36 = Entry(root, width=15)
entry_36.grid(row=11, column=7)

label_41 = Label(root, text="Subscription Received in advance  ")
label_41.grid(row=12, sticky=E, column=6)
entry_37 = Entry(root, width=15)
entry_37.grid(row=12, column=7)

label_42 = Label(root, text="Stationary & Postage")
label_42.grid(row=13, sticky=E, column=6)
entry_38 = Entry(root, width=15)
entry_38.grid(row=13, column=7)

label_43 = Label(root, text="Tournament Fund")
label_43.grid(row=14, sticky=E, column=6)
entry_39 = Entry(root, width=15)
entry_39.grid(row=14, column=7)

label_44 = Label(root, text="Stock of medicines")
label_44.grid(row=15, sticky=E, column=6)
entry_40 = Entry(root, width=15)
entry_40.grid(row=15, column=7)


label_45 = Label(root,font = ("courier",18,"bold"),text="Add-Info")
label_45.grid(row=1, column= 9)

label_46 = Label(root, text="Dep on Building in %")
label_46.grid(row=4, sticky=E, column=8)
entry_41 = Entry(root, width=15)
entry_41.grid(row=4, column=9)

label_47 = Label(root, text="Dep on Furniture in % ")
label_47.grid(row=5, sticky=E, column=8)
entry_42 = Entry(root, width=15)
entry_42.grid(row=5, column=9)

label_48 = Label(root, text="Written-off on Books ")
label_48.grid(row=6, sticky=E, column=8)
entry_43 = Entry(root, width=15)
entry_43.grid(row=6, column=9)

label_49 = Label(root, text="Subs Outstanding")
label_49.grid(row=7, sticky=E, column=8)
entry_44 = Entry(root, width=15)
entry_44.grid(row=7, column=9)

label_50 = Label(root, text="Subs Cr Advance")
label_50.grid(row=8, sticky=E, column=8)
entry_45 = Entry(root, width=15)
entry_45.grid(row=8, column=9)
    
label_51 = Label(root, text="Cash in hand")
label_51.grid(row=9, sticky=E, column=8)
entry_46 = Entry(root, width=15)
entry_46.grid(row=9, column=9)

label_52 = Label(root, text="Cash at bank")
label_52.grid(row=10, sticky=E, column=8)
entry_47 = Entry(root, width=15)
entry_47.grid(row=10, column=9)

label_53 = Label(root, text="Dr over Sports fund")
label_53.grid(row=11, sticky=E, column=8)
entry_48 = Entry(root, width=15)
entry_48.grid(row=11, column=9)

label_54 = Label(root, text="Dr over tournament fund")
label_54.grid(row=12, sticky=E, column=8)
entry_49 = Entry(root, width=15)
entry_49.grid(row=12, column=9)

label_55 = Label(root, text="O/S Wages & Salary")
label_55.grid(row=13, sticky=E, column=8)
entry_50 = Entry(root, width=15)
entry_50.grid(row=13, column=9)

label_56 = Label(root, text="Adv Wages & Salary")
label_56.grid(row=14, sticky=E, column=8)
entry_51 = Entry(root, width=15)
entry_51.grid(row=14, column=9)
    
label_57 = Label(root, text="Stationary&Postage")
label_57.grid(row=15, sticky=E, column=8)
entry_52 = Entry(root, width=15)
entry_52.grid(row=15, column=9)



button1 = Button(root, text="Submit Data",command=calculation)
button1.grid(row=18, column=9)

root.mainloop()
#messagebox.showwarning("Warning","This accounting software is strictly for Not-For-Profit-Organaisation It doesn't Support accounts for profit based firms")