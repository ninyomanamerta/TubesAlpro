import connect as conData
from prettytable import PrettyTable
import utils.dateUtils as dateUtil
import visualData as visData

def showDataMsNegara() :
    prettyTab = PrettyTable()
    prettyTab.field_names = ["ID", "NEGARA", "BENUA"]
    for x in conData.getMasterNegara():
        prettyTab.add_row([x[0], x[1], x[2]])
    print (prettyTab)

def showDataMsBenua() :
    prettyTab2 = PrettyTable()
    prettyTab2.field_names = ["ID", "BENUA"]
    for x in conData.getMasterBenua():
        prettyTab2.add_row([x[0], x[1]])
    print (prettyTab2)

def showDataCustomer():
    prettyTab1 = PrettyTable()
    prettyTab1.field_names = ["ID", "NAMA", "DOB", "UMUR", "NEGARA", "BENUA", "JOB", "REGISTER_DATE"]
    for x in conData.getDataCustomer():
        prettyTab1.add_row([x[0], x[1], x[2].strftime('%Y-%m-%d'), x[3], x[4], x[5], x[6], x[7].strftime('%Y-%m-%d %H:%M:%S')])
    print(prettyTab1)

repeatMenu='Yes'
while(repeatMenu=='Yes'):
	print("======================")
	print("\tMENU")
	print("======================")
	print("1. Show Data")
	print("2. Add Data Customer")
	print("3. Add Data Negara")
	print("4. Visual Data")
	print("5. Exit\n")
	varin = input("Please select menu [1..5] : ")
	tempVarIn=int(varin)
	if tempVarIn < 6 :
		repeatMenu = 'No'
 
	if str(varin) == '1' :
		repeatMethod = 'Yes'
		while(repeatMethod == 'Yes'):
			print("======= LIST DATA CUSTOMER =======")
			showDataCustomer()
			print("\n======= LIST DATA NEGARA =======")
			showDataMsNegara()
			isContinue = input("Do you want to continue [Yes/No] : ")
			repeatMethod = isContinue
		repeatMenu='Yes'
	elif str(varin) == '2' :
		repeatMethod = 'Yes'
		while(repeatMethod == 'Yes'):
			print("======= ADD DATA CUSTOMER ========\n")
			nameCust = input("Please input customer name : ")
			dobCust = input("Please input date of birth customer : ")
			while(True):
				if (dateUtil.is_valid_date(dobCust)==True) :
					break
				else :
					print("Dob format not valid, please input valid date format ...!!!")
					dobCust = input("Please input date of birth customer : ")

			print("--------- List Negara --------")
			showDataMsNegara()
			negara_cust = int(input("Please input negara id : "))
			while(True):
				if (conData.checkIdNegaraExists(negara_cust)[0]==0) :
					print("Negara does not exists, please select on value above ...!!!")
					negara_cust = int(input("Please input negara id : "))
				else :
					break
			job_cust = input("Please input job customer : ")
			isOk = input("Are you sure for this data [Yes/No] : ")
			if isOk == 'Yes' :
				#dobCustDate = dobCust.strftime('%Y-%m-%d')
				result = conData.insertDataCustomer(nameCust, dobCust, negara_cust, job_cust)
				if result == 1 :
					print("Data customer has been added successfully")
				else :
					print("Failed add data customer")
				isContinue = input("Do you want to continue [Yes/No] : ")
				repeatMethod = isContinue
			else :
				isContinue = input("Do you want to continue [Yes/No] : ")
				repeatMethod = isContinue
		repeatMenu='Yes'
	elif str(varin) == '3' :
		repeatMethod = 'Yes'
		while(repeatMethod == 'Yes'):
			print("======= ADD DATA NEGARA ========\n")
			negara = input("Please input negara name : ")
			while(True):
				if (conData.checkNegaraNameExists(negara)[0]==0) :
					break	
				else :
					print("Negara already exists...!!!")
					negara = input("Please input negara name : ")
			print("--------- List Benua --------")
			showDataMsBenua()
			benua = input("Please input id benua : ")
			while(True):
				if (conData.checkIdBenuaExists(benua)[0]==0) :
					print("Benua does not exists, please select on value above ...!!!")
					benua = input("Please input id benua : ")
				else :
					break
			isOk = input("Are you sure for this data [Yes/No] : ")
			if isOk == 'Yes' :
				result = conData.insertDataNegara(negara, benua)
				if result == 1 :
					print("Data negara has been added successfully")
				else :
					print("Failed add data negara into db")
				isContinue = input("Do you want to continue [Yes/No] : ")
				repeatMethod = isContinue
			else :
				isContinue = input("Do you want to continue [Yes/No] : ")
				repeatMethod = isContinue
		repeatMenu='Yes'
	elif str(varin) == '4' :
		print("Visual Data\n")
		repeatMethod = 'Yes'
		while(repeatMethod == 'Yes'):
			visData.visualCustByNegara()
			isContinue = input("Do you want to continue [Yes/No] : ")
			repeatMethod = isContinue
		repeatMenu='Yes'
	elif str(varin) == '5' :
		print("Exit from program\n")
		break
	else :
		repeatMenu='Yes'