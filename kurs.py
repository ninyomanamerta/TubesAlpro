import connect as conData
from prettytable import PrettyTable
import utils.dateUtils as dateUtil
import visualData as visData

def showDataMsCurrency() :
    prettyTab = PrettyTable()
    prettyTab.field_names = ["ID", "KODE", "KETERANGAN"]
    for x in conData.getMasterCurrency():
        prettyTab.add_row([x[0], x[1], x[2]])
    print (prettyTab)

def showDataMsCurrencyById(idCurr) :
    prettyTab1 = PrettyTable()
    prettyTab1.field_names = ["ID", "KODE", "KETERANGAN"]
    for x in conData.getMasterCurrencyById(idCurr):
        prettyTab1.add_row([x[0], x[1], x[2]])
    print (prettyTab1)

def deleteCurrData(id) :
    result="Currency Id already used i detail kurs"
    if conData.getDetailKursByCurrId(id)[0]<1 :
        exec = conData.deleteMasterCurrency(id)
        if exec==1 :
            result="1"
        else :
            result="Failed delete data"
    return result

def updateCurrData(kode, keterangan, id):
    result=""
    if conData.checkCurrIdExists(id)[0]>0 :
        exec = conData.updateMasterCurrency(kode, keterangan, id)
        if exec == 1 :
            result="1"
        else :
            result="Failed update data"
    else :
        result="Id not found"
    return result

def insertCurrData(kode, keterangan):
    result=""
    exec=conData.insertMasterCurrency(kode, keterangan)
    if exec==1 :
        result="1"
    else :
        result="Failed insert data"
    return result

#================= ABOUT KURS =======================================
def insertKursValue(kode, nominal, insertDate):
    result=""
    exec=conData.insertDetailKurs(kode, nominal, insertDate)
    if exec==1 :
        result="1"
    else :
        result="Failed insert data"
    return result

def showDataKurs() :
    prettyTabKurs = PrettyTable()
    prettyTabKurs.field_names = ["ID", "KODE", "NOMINAL", "INSERT DATE"]
    for x in conData.getDetailKurs():
        prettyTabKurs.add_row([x[0], x[1], x[2], x[3]])
    print (prettyTabKurs)

def showDataKursById(id) :
    prettyTabKursId = PrettyTable()
    prettyTabKursId.field_names = ["ID", "KODE", "NOMINAL", "INSERT DATE"]
    for x in conData.getDetailKursById(id):
        prettyTabKursId.add_row([x[0], x[1], x[2], x[3]])
    print (prettyTabKursId)

def deleteKurs(id) :
    result=""
    exec = conData.deleteDetailKurs(id)
    if exec==1 :
        result="1"
    else :
        result="Failed delete data"
    return result

def updateNominalKurs(id, nominal):
    result=""
    if conData.checkKursIdExists(id)[0]>0 :
        exec = conData.updateDetailKursNominal(id, nominal)
        if exec == 1 :
            result="1"
        else :
            result="Failed update data"
    else :
        result="Id not found"
    return result

#========== MENU FOR KURS =================================================
def menu_kurs():
    while(True):
        print("======================")
        print("\tMENU")
        print("======================")
        print("1. Show Data")
        print("2. Add Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Visual Data")
        print("6. Exit\n")
        varin = input("Please select menu [1..6] : ")
        
        if varin == '1' :
            while(True):
                print("======= LIST DATA CURRENCY =======")
                showDataMsCurrency()
                print("\n======= LIST DATA KURS =======")
                showDataKurs()
                isContinue = input("Do you want to continue [Yes/No] : ")
                if isContinue=='No' :
                    break
        elif varin == '2' :
            while(True):
                print("======================")
                print("\tADD DATA MENU")
                print("======================")
                print("1. Add Currency")
                print("2. Add Kurs")
                print("3. Back\n")
                varinAdd = input("Please select menu [1..3] : ")
                if varinAdd == '1':
                    while(True):
                        print("======= ADD DATA MASTER CURRENCY ========\n")
                        kodeCurr = input("Please input currency code : ")
                        keterangan = input("Please input keterangan : ")
                        isOk = input("Are you sure for this data [Yes/No] : ")
                        if isOk == 'Yes' :
                            addToDbCurr = insertCurrData(kodeCurr, keterangan)
                            if addToDbCurr == '1':
                                print("Success add data to master currency")
                            else :
                                print(addToDbCurr)
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                        else :
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                elif varinAdd == '2' :
                    while(True):
                        print("======= ADD DATA KURS ========\n")
                        print("--------- LIST MASTER CURRENCY ------------")
                        showDataMsCurrency()
                        kodeCurr = input("Please input currency id : ")
                        while(True):
                            if conData.checkCurrIdExists(kodeCurr)[0]==0 :
                                print("Currency ID not valid, please input valid ID")
                                kodeCurr = input("Please input currency code : ")
                            else :
                                break
                        nominal = int(input("Please input nominal : "))
                        insertDate = input("Please input insert date [yyyy-MM-dd] : ")
                        while(True):
                            if (dateUtil.is_valid_date(insertDate)==True) :
                                break
                            else :
                                print("Date format not valid, please input valid date format ...!!!")
                                insertDate = input("Please input insert date [yyyy-MM-dd] : ")
                        isOk = input("Are you sure for this data [Yes/No] : ")
                        if isOk == 'Yes' :
                            addToDb = insertKursValue(kodeCurr, nominal, insertDate)
                            if addToDb == '1':
                                print("Success add data to kurs db")
                            else :
                                print(addToDb)
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                        else :
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                elif varinAdd=='3' :
                    break
                else :
                    print("Please input valid menu\n")

               
        elif varin == '3' :
            while(True):
                print("======================")
                print("\tUPDATE DATA MENU")
                print("======================")
                print("1. Update Currency")
                print("2. Update Kurs")
                print("3. Back\n")
                varinUpdate = input("Please select menu [1..3] : ")
                if varinUpdate == '1':
                    while(True):
                        print("======= UPDATE DATA MASTER CURRENCY ========\n")
                        print("--------- LIST MASTER CURRENCY ------------")
                        showDataMsCurrency()
                        kodeCurrid = input("Please select currency id which want to update : ")
                        while(True):
                            if conData.checkCurrIdExists(kodeCurrid)[0]==0 :
                                print("Currency ID not valid, please input valid ID")
                                kodeCurrid = input("Please select currency id which want to update : ")
                            else :
                                break
                        print("--------- CURRENCY YOU ARE SELECTED ------------")
                        showDataMsCurrencyById(kodeCurrid)
                        kodeCurr = input("Please input new currency code : ")
                        keterangan = input("Please input keterangan : ")
                        isOk = input("Are you sure for this data [Yes/No] : ")
                        if isOk == 'Yes' :
                            updateToDbCurr = updateCurrData(kodeCurr, keterangan, kodeCurrid)
                            if updateToDbCurr == '1':
                                print("Success update data to master currency")
                            else :
                                print(updateToDbCurr)
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                        else :
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                elif varinUpdate == '2' :
                    while(True):
                        print("======= UPDATE DATA KURS ========\n")
                        print("--------- LIST DATA KURS ------------")
                        showDataKurs()
                        kursId = input("Please select kurs id which want to update nominal : ")
                        while(True):
                            if conData.checkKursIdExists(kursId)[0]==0 :
                                print("Kurs ID not valid, please input valid ID")
                                kursId = input("Please select kurs id which want to update nominal : ")
                            else :
                                break
                        print("--------- DATA KURS SELECTED ------------")
                        showDataKursById(kursId)
                        nominal = int(input("Please input new nominal : "))
                        
                        isOk = input("Are you sure for this data [Yes/No] : ")
                        if isOk == 'Yes' :
                            addToDb = updateNominalKurs(kursId, nominal)
                            if addToDb == '1':
                                print("Success update data nominal to kurs db")
                            else :
                                print(addToDb)
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                        else :
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                elif varinUpdate=='3' :
                    break
                else :
                    print("Please input valid menu\n")

        elif varin == '4' :
            while(True):
                print("======================")
                print("\tDELETE DATA MENU")
                print("======================")
                print("1. Delete Currency")
                print("2. Delete Kurs")
                print("3. Back\n")
                varinDel = input("Please select menu [1..3] : ")
                if varinDel == '1':
                    while(True):
                        print("======= UPDATE DATA MASTER CURRENCY ========\n")
                        print("--------- LIST MASTER CURRENCY ------------")
                        showDataMsCurrency()
                        kodeCurrid = input("Please select currency id which want to delete : ")
                        while(True):
                            if conData.checkCurrIdExists(kodeCurrid)[0]==0 :
                                print("Currency ID not valid, please input valid ID")
                                kodeCurrid = input("Please select currency id which want to delete : ")
                            else :
                                break
                        print("--------- CURRENCY YOU ARE SELECTED ------------")
                        showDataMsCurrencyById(kodeCurrid)
                        isOk = input("Are you sure for this data [Yes/No] : ")
                        if isOk == 'Yes' :
                            delete = deleteCurrData(kodeCurrid)
                            if delete == '1':
                                print("Success delete data master currency")
                            else :
                                print(delete)
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                        else :
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                elif varinDel == '2' :
                    while(True):
                        print("======= UPDATE DATA KURS ========\n")
                        print("--------- LIST DATA KURS ------------")
                        showDataKurs()
                        kursId = input("Please select kurs id which want to delete : ")
                        while(True):
                            if conData.checkKursIdExists(kursId)[0]==0 :
                                print("Kurs ID not valid, please input valid ID")
                                kursId = input("Please select kurs id which want to delete : ")
                            else :
                                break
                        print("--------- DATA KURS SELECTED ------------")
                        showDataKursById(kursId)
                        isOk = input("Are you sure for this data [Yes/No] : ")
                        if isOk == 'Yes' :
                            addToDb = deleteKurs(kursId)
                            if addToDb == '1':
                                print("Success delete data kurs db")
                            else :
                                print(addToDb)
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                        else :
                            isContinue = input("Do you want to continue [Yes/No] : ")
                            if isContinue == 'No' :
                                break
                elif varinDel=='3' :
                    break
                else :
                    print("Please input valid menu\n")

        elif varin == '5' :
            print("Visual Data\n")
            while(True):
                visData.visualKurs()
                isContinue = input("Do you want to continue [Yes/No] : ")
                if isContinue == 'No' :
                    break
        elif varin == '6' :
            print("Exit from program\n")
            break
        else :
            print("Please input valid menu\n")
menu_kurs()