from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import connect as conData

def visualCustByNegara():
    #y = np.array([35, 25, 25, 15])
    count=[]
    negara=[]
    for x in conData.getVisualCustomerByNegara():
        count.append(x[1])
        negara.append(x[0])
    y = np.array(count)
	#mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
    #mylabels = conData.getVisualCustomerByNegara[0]
    plt.pie(y, labels = negara, startangle=90, autopct='%1.1f%%', shadow=True)
    plt.title("Visual customer based on Negara")
    plt.show() 
def uniqueish_color():
    return plt.cm.gist_ncar(np.random.random())

def visualKurs() :
    Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
    Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
    Unemployment_Rate1 = [14,5,8,3,13,8,9,3,5,4]
    #num_plots = 20
    #colormap = plt.cm.gist_ncar
    #plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, num_plots))))
    plt.plot(Year, Unemployment_Rate, color=uniqueish_color(), marker='o')
    plt.plot(Year, Unemployment_Rate1, color=uniqueish_color(), marker='o')
    plt.title('Unemployment Rate Vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Rate', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()