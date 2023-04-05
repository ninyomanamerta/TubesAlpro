import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kurs_db_apps"
)

mycursor = mydb.cursor()

def getMasterNegara() :
    mycursor.execute("SELECT msn.Id_Negara, msn.Negara, msb.Nama_Benua as Benua FROM master_negara msn join master_benua msb on msn.Benua=msb.Id_Benua order by msn.Id_Negara")
    myresult = mycursor.fetchall()
    return myresult

def checkIdNegaraExists(id):
    mycursor.execute("SELECT count(*) as jumlah FROM master_negara WHERE Id_Negara = %s",(id,))
    myresult = mycursor.fetchone()
    return myresult

def checkNegaraNameExists(name):
    mycursor.execute("SELECT count(*) as jumlah FROM master_negara WHERE Negara = %s",(name,))
    myresult = mycursor.fetchone()
    return myresult

def getMasterBenua() :
    mycursor.execute("SELECT * FROM master_benua")
    myresult = mycursor.fetchall()
    return myresult

def checkIdBenuaExists(id):
    mycursor.execute("SELECT count(*) as jumlah FROM master_benua WHERE Id_Benua = %s",(id,))
    myresult = mycursor.fetchone()
    return myresult

def getDataCustomer() :
    mycursor.execute("SELECT pc.Id_Customer, pc.Nama_Customer, pc.Dob_Customer, YEAR(NOW()) - YEAR(pc.Dob_Customer) - (DATE_FORMAT(NOW(), '%m%d') < DATE_FORMAT(pc.Dob_Customer, '%m%d')) AS Age_Customer, msn.Negara AS Negara_Customer, msb.Nama_Benua AS Benua_Customer, pc.Job_Customer, pc.Register_Date FROM profile_customer pc JOIN master_negara msn ON pc.Negara_Customer=msn.Id_Negara join master_benua msb on msn.Benua=msb.Id_Benua")
    myresult = mycursor.fetchall()
    return myresult

def getVisualCustomerByNegara():
    mycursor.execute("SELECT msn.Negara AS Negara_Customer, COUNT(*) AS Jumlah FROM profile_customer pc JOIN master_negara msn ON pc.Negara_Customer=msn.Id_Negara Group BY msn.Negara")
    myresult = mycursor.fetchall()
    return myresult

def insertDataCustomer(name, dob, idNegara, job):
    result=0
    try :
        mycursor.execute("INSERT INTO profile_customer (Nama_Customer, Dob_Customer, Negara_Customer, Job_Customer, Register_Date) VALUES (%s, str_to_date(%s,'%Y-%m-%d'), %s, %s, now())",(name, dob, idNegara, job))
        mydb.commit()
        result=1
        return result
    except Exception as e :
        print(e)
        return result

def updateDataCustomer(id, name, dob, idNegara, job):
    result=0
    try :
        mycursor.execute("update profile_customer set Nama_Customer=%s, Dob_Customer=str_to_date(%s,'%Y-%m-%d'), Negara_Customer=%s, Job_Customer=%s where Id_Customer=%s",(name, dob, idNegara, job, id))
        mydb.commit()
        result=1
        return result
    except Exception as e :
        print(e)
        return result

def deleteDataCustomer(id) :
    result=0
    try :
        mycursor.execute("DELETE FROM profile_customer where Id_Customer= %s",(id,))
        mydb.commit()
        result=1
        return result
    except :
        return result

def insertDataNegara(name, benua):
    result=0
    try :
        mycursor.execute("INSERT INTO master_negara (Negara, Benua, Created_Date) VALUES (%s, %s, now())",(name, benua))
        mydb.commit()
        result=1
        return result
    except :
        return result
#================================ ALL ABOUT MASTER CURRENCY ====================================
def insertMasterCurrency(kode, keterangan):
    result=0
    try :
        mycursor.execute("INSERT INTO master_currency (Kode_Currency, Keterangan, Created_Date) VALUES (%s, %s, now())",(kode, keterangan))
        mydb.commit()
        result=1
        return result
    except :
        return result

def getMasterCurrency() :
    mycursor.execute("SELECT * FROM master_currency order by Currency_Id")
    myresult = mycursor.fetchall()
    return myresult

def getMasterCurrencyById(id) :
    mycursor.execute("SELECT * FROM master_currency where Currency_Id= %s",(id,))
    myresult = mycursor.fetchall()
    return myresult

def checkCurrIdExists(id) :
    mycursor.execute("SELECT count(*) as ROW_DATA FROM master_currency where Currency_Id= %s",(id,))
    myresult = mycursor.fetchone()
    return myresult

def deleteMasterCurrency(id) :
    result=0
    try :
        mycursor.execute("DELETE FROM master_currency where Currency_Id= %s",(id,))
        mydb.commit()
        result=1
        return result
    except :
        return result

def updateMasterCurrency(kode, keterangan, id) :
    result=0
    try :
        mycursor.execute("UPDATE master_currency SET Kode_Currency=%s, Keterangan=%s where Currency_Id= %s",(kode, keterangan, id))
        mydb.commit()
        result=1
        return result
    except :
        return result

#================================ ALL ABOUT DETAIL KURS ====================================
def insertDetailKurs(kode, nominal, insertDate):
    result=0
    try :
        mycursor.execute("INSERT INTO detail_kurs (Currency_Id, Insert_Date, Nominal) VALUES (%s, str_to_date(%s,'%Y-%m-%d'), %s)",(kode, insertDate, nominal))
        mydb.commit()
        result=1
        return result
    except :
        return result

def getDetailKurs() :
    mycursor.execute("SELECT dk.Kurs_Id, mc.Kode_Currency, dk.Nominal, dk.Insert_Date FROM detail_kurs dk join master_currency mc on dk.Currency_Id=mc.Currency_Id order by dk.Kurs_Id")
    myresult = mycursor.fetchall()
    return myresult

def getDetailKursByCurrId(id) :
    mycursor.execute("SELECT count(*) as Row_Date FROM detail_kurs dk join master_currency mc on dk.Currency_Id=mc.Currency_Id where dk.Currency_Id= %s",(id,))
    myresult = mycursor.fetchone()
    return myresult

def getDetailKursById(id) :
    mycursor.execute("SELECT dk.Kurs_Id, mc.Kode_Currency, dk.Nominal, dk.Insert_Date FROM detail_kurs dk join master_currency mc on dk.Currency_Id=mc.Currency_Id where dk.Kurs_Id= %s",(id,))
    myresult = mycursor.fetchone()
    return myresult

def deleteDetailKurs(id) :
    result=0
    try :
        mycursor.execute("DELETE FROM detail_kurs where Kurs_Id= %s",(id,))
        mydb.commit()
        result=1
        return result
    except :
        return result

def updateDetailKursNominal(id, nominal) :
    result=0
    try :
        mycursor.execute("UPDATE detail_kurs SET Nominal=%s where Kurs_Id= %s",(nominal, id))
        mydb.commit()
        result=1
        return result
    except :
        return result
