import binance
from datetime import datetime
import sys
import time

def getPrices(): #Returns a dictionary
    currentPriceDictionary = binance.prices()
    #We have a dictionary {'ETHBTC': '0.02198200', 'LTCBTC': '0.00945600'...}
    #print(priceList['ETHBTC'])
    return currentPriceDictionary #A Dictionary

def setFavorites():
    '''
    print("What are your favorite coin? The format needed is something converted to something, so BNBBTC or ZECUSDC")
    read answer
    #Delit using the spaces, then make it a list.
    favorites = list(answer.split(" "))
    return favorites

    '''
    favorites = ["BTCUSDC", "ZECUSDC", "NPXSBTC"] #Add your favorite coins to be printed here.
    verifyInput(favorites)
    return favorites #A List

def verifyInput(favorites):
    current = getPrices()
    try:
        for item in favorites:
            verified = current[item]
            print(item + " looks good at " + verified)

    except:
        print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
        print("ERROR ERROR ERROR: A value you entered does not match the format of any existing currency:ERROR ERROR ERROR")
        print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
        print(item + " has been input incorrectly.")
        print("Exiting program.")
        exit()
    print("Your favorites have been set.")
    print("Pres Enter to continue...")
    trash = input()
    sys.stdout.write("\033[2J")  # Erase everything

def printCurrentFavorites(): #Prints the current favorite coins
    current = getPrices()
    favorites = getFavorites()

    for item in favorites:
        print(item + ": " + current[item])
    time.sleep(1)

def printToScreen(currentItem,run,favSize):
    count = 0
    favSize = favSize - 1
    #favSize = favSize+1 #Add one to include the Time Update
    if run is not favSize:
        sys.stdout.write("\r{0}\n".format(currentItem))
    else:
        sys.stdout.write("\r{0}".format(currentItem))

        '''sys.stdout.write("\033[{0}A".format(favSize))'''
        ''''#while count > favSize: #Go back to the top where everything started
        sys.stdout.write("\033[1A")
        count = count + 1
        '''

def getDateTime():
    while True:
        now = datetime.now()  # Get the date and time
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        time.sleep(1)

def printCurrentFavorites(favorites,goTo): #Prints the current favorite coins
    while True:
        try:
            sys.stdout.write("\033[2J") #Erase everything
            now = datetime.now() #Get the date and time
            theTime = now.strftime("%d/%m/%Y %H:%M:%S")
            current = "Deleted" #Erase the previous entry
            current = getPrices() #Get the current Prices. Binance returns all coins avaiable.
            favSize = len(favorites)

            UpdateTime = "\nUpdate: " + theTime + "\n"
            print(UpdateTime)

            for count, item in enumerate(favorites):
                currentItem = item + ": " + current[item]
                printToScreen(currentItem,count,favSize)
                sys.stdout.flush()
            time.sleep(2)
        except:
            print("Going to main manu:")
            if goTo is "limited":
                limitedMenu(favorites)
            else:
                fullMenu(favorites)

def getAPI():
    #Input your API keys here.
    # Set the keys. binance.set("API Key","Secret")
    APIKey = "5GYxIkoBqCQJMzgqZH2sf193FFTVQX52MNVsdNamGpofoFVSm2ftIqyFemvkmQPP"
    APISecret = "3t6AkChBnIaDHwzSzdTZUU6m550Q2B3KCBpw8nNpK0giSLSkw2m4loP9NiHkoOXJ"

    #APIKey = "INPUT_KEY_HERE"
    #APISecret = "INPUT_SECRET_HERE"

    if APIKey is "INPUT_KEY_HERE" or APISecret is "INPUT_SECRET_HERE":
        print("WARNING: You did not input your API keys. All this program can do for you is show you current prices")
        return 0

    binance.set("5GYxIkoBqCQJMzgqZH2sf193FFTVQX52MNVsdNamGpofoFVSm2ftIqyFemvkmQPP", "3t6AkChBnIaDHwzSzdTZUU6m550Q2B3KCBpw8nNpK0giSLSkw2m4loP9NiHkoOXJ")
    #binance.set(APIKey, APISecret)
    print("Your keys are all set.")
    return 1

def Banner():
    print("######################################################################################")
    print("###########################Crypto Trader for Binance##################################")
    print("######################################################################################")
    print("Welcome to Crypto Trader for Binance.")
    print("The creator of this script is not responsible for the stupid things you can do with it")
    print("Be smart with your money.")
    print("Press Enter to continue...")
    input()
    sys.stdout.write("\033[2J")  # Erase everything

def limitedMenu(Favorites):
    print("Welcome to the Main Menu.")
    print("What would you like to do?")
    print("Input \"P\" to get current prices for your favorites.")
    print("Input \"e\" to end the program.")
    answer = input()
    if answer is "P" or answer is "p":
        sys.stdout.write("\033[2J")  # Erase everything
        printCurrentFavorites(Favorites,"limited")
    elif answer is "k" or answer is "K":  # Look at open and closes on currencies in the last minute.
        binance.klines("BNBBTC", "1m")
    elif answer is "e" or answer is "exit":
        exit()
    else:
        print("You input something funky. Please try again.\n\n")
        limitedMenu(Favorites)

def fullMenu(Favorites):
    print("Welcome to the Main Menu.")
    print("What would you like to do?")
    print("Input \"P\" to get current prices for your favorites.")
    print("Input \"e\" to end the program.")
    print("Input \"b\" to check the current balances on your account.")
    print("Input \"o\" to place an order.")
    print("Input \"c\" to cancel an order.")
    print("Input \"s\" to view open order status.")
    print("Input \"a\" to view all orders open or closed.")
    answer = input()

    if answer is "P" or answer is "p": #Look at Current Prices
        sys.stdout.write("\033[2J")  # Erase everything
        printCurrentFavorites(Favorites,"full")
    elif answer is "k" or answer is "K":  # Look at open and closes on currencies in the last minute.
        binance.klines("BNBBTC", "1m")
    elif answer is "b" or answer is "B":  # Look at Current Balances on account
        binance.balances()
    elif answer is "o" or answer is "O":  # Place an order. Make sure this pulls up enough data for the user to know what they're doing.
        binance.order("BTCUSDC", binance.BUY, 1000, 0.000001) #Display favorites and maybe show the last hour of data
    elif answer is "c" or answer is "C": #Cancel and order. Make sure to show current orders.
        binance.cancel("BTCUSDC", orderId=123456789)
    elif answer is "s" or answer is "S":  # View open orders. This command must be run for each currency.
        binance.openOrders("BTCUSDC")
    elif answer is "a" or answer is "A": #View all orders open or closed. Must run for each currency.
        binance.allOrders("BTCUSDC")
    elif answer is "e" or answer is "exit": #Exit
        exit()
    else:
        print("You input something funky. Please try again.\n\n")
        fullMenu(Favorites)

###################################################################################################
##############The###########################Main###############################Code################
###################################################################################################

Banner() #Print Banner
avaiableFeatures = getAPI() #Set API for the program.
Favorites = setFavorites()
if avaiableFeatures is 0: #If the user does not have API Keys
    limitedMenu(Favorites)

else: #If the user has API Keys
    fullMenu(Favorites)
