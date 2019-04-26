from menu import printMenu, callMenu

chooseMenu = 0
while(chooseMenu != 3):
    chooseMenu = printMenu()
    callMenu(chooseMenu)
