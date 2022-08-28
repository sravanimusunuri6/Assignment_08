#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Sravani Musunuri, 2020-Aug-27, upating the CD Inventory program to make it work.
#------------------------------------------#


# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD(object):

    """Stores data about a CD:
    
    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        None
    """
    
    ## -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = int(value)

    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        self.__title = str(value)

    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = str(value)

# -- PROCESSING -- #

class DataProcessor:
    """Processing the data to add and delete an item from the List of Dictionaries:
    
        properties:
            None

        methods:
            add_inventory(cd_id, cd_title, cd_artist, lstCDObj) -> (a list of CD objects)
            del_inventory(lstCDObj) -> (a list of CD objects)
    
    """  
    
    @staticmethod
    def add_inventory(cd_id, cd_title, cd_artist, lstCDObj):
        """Function to manage user input ingestion to a list

        User Input is added to a 2D table.

        Args:
            cd_id (string): ID of CD Inventory
            cd_title (string): Title of CD Inventory
            cd_artist (string): Artist of the CD Inventory

        Returns:
            2D List.
        """
        
        addCDObj = CD(cd_id, cd_title, cd_artist)
        lstCDObj.append(addCDObj)
        
        return lstCDObj

    @staticmethod
    def delete_inventory(lstCDObj, intIDDel):
        """Function to manage deletion of an item from a list of dictionaries

        Delete an item by parsing thru the 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            lstTbl (list of dictionaries): List of CD inventories
            intIDDel (int): ID of CD Inventory

        Returns:
            2D table (list of dict).
            
        """
        
        intRowNr = -1
        blnCDRemoved = False
        for row in lstCDObj:
            intRowNr += 1
            if row.cd_id  == intIDDel:
                del lstCDObj[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
            
        return lstCDObj
    
    

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name, lst_Inventory): -> (a list of CD objects)

    """

    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to save binary data to the file identified by file_name into a 2D lstOfCDObjects

       Args:
           file_name (string): name of file used to read the data from
           lst_Inventory: 2D data structure (list of objects) that holds the data during runtime

       Returns:
           None.
       """
                
                
        with open(file_name,'w') as objFile:
            for row in lst_Inventory:
                cdRow = [row.cd_id, row.cd_title, row.cd_artist]
                lstValues = list(cdRow)
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
        

    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        """Function to manage binary data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D lstOfCDObjects
        (list of dicts) lst_Inventory one line in the file represents one dictionary row in lst_Inventory.

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory: 2D data structure (list of objects) that holds the data during runtime

        Returns:
            lst_Inventory.
        """
        # Making sure the program won't crash if file doesn't exist.

        try:
            
            lst_Inventory.clear()
            with open(file_name, 'r') as objFile:    
                for row in objFile:
                    row = row.strip().split(',')
                    cd_id,cd_title,cd_artist = int(row[0]),row[1],row[2]
                    addObj = CD(cd_id,cd_title,cd_artist)
                    lst_Inventory.append(addObj)
                
        except FileNotFoundError:
            print()
            print('[ERROR] ',file_name,'does not exit in current directory')
            print()
            
        return lst_Inventory


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output:

    properties:

    methods:
        print_menu(): -> None
        menu_choice(): -> None
        show_inventory(): -> None
        user_input(): -> None

    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(lstCDObj):
        """Displays current inventory table


        Args:
            lstCDObj: 2D data structure (list of objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lstCDObj:
            print('{}\t{} (by:{})'.format(row.cd_id, row.cd_title, row.cd_artist))
        print('======================================')

    @staticmethod
    def user_input():
        """Gets user input for CD Inventory

        Args:
            None.

        Returns:
            strID (string): ID of CD Inventory
            strTitle (string): Title of CD Inventory
            strArtist (string): Artist of the CD Inventory

        """
        while True:
            try:
                strID = int(input('Enter ID: ').strip())
                
                if strID <= 0:
                    print()
                    raise Exception('[ERROR] Inventory ID cannot be 0 or less. Please enter valid Inventory details.')
                
                
                strTitle = input('What is the CD\'s title? ').strip()
                
                if strTitle == "":
                    print()
                    raise Exception('[ERROR] CD Title cannot be NULL. Please enter valid Inventory details.')
                
                strArtist = input('What is the Artist\'s name? ').strip()          
                
                
                if strArtist == "":
                    raise Exception('[ERROR] Artist Name cannot be NULL. Please enter valid Inventory details.')

                print()
                
                return strID,strTitle,strArtist
                
            except ValueError:
                print()
                print("[ERROR] That is not an integer! Please enter an integer when prompted to enter ID.")
                print()
                
            except Exception as e:
                print()
                print(e)
                print()


# 1. When program starts, read in the currently saved Inventory
lstOfCDObjects = FileIO.load_inventory(strFileName,lstOfCDObjects)

# 2. start main loop
while True:
    
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    
    # 3.2 process load inventory
    if strChoice == 'l':
        
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        
        if strYesNo.lower() == 'yes':
            print('reloading...')
            
            lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
            
            IO.show_inventory(lstOfCDObjects)
            
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            
            IO.show_inventory(lstOfCDObjects)
            
        continue  # start loop back at top.
        
    # 3.3 process add a CD
    elif strChoice == 'a':
        
        #Getting User Input
        strID,strTitle,strArtist = IO.user_input()
        
        #Calling the function to add item to the table
        lstOfCDObjects = DataProcessor.add_inventory(strID,strTitle,strArtist,lstOfCDObjects)
        
        #Display the CD Inventory
        IO.show_inventory(lstOfCDObjects)
        
        continue  # start loop back at top.
        
    # 3.4 process display current inventory
    elif strChoice == 'i':
        
        IO.show_inventory(lstOfCDObjects)
        
        continue  # start loop back at top.
        
    # 3.5 process delete a CD
    elif strChoice == 'd':
        
        #Get Userinput for which CD to delete
        #Display Inventory to user
        IO.show_inventory(lstOfCDObjects)
        
        #Ask user which ID to remove
        intIDDel = input('Which ID would you like to delete? ').strip()
        
        try:
            #Ask user which ID to remove
            intIDDel = int(intIDDel)
            
        except ValueError:
            print()
            print("[ERROR] That is not an integer! Please enter an integer when prompted to enter ID.")
            print()
            continue
        
        #Calling the function to delete an item from the Inventory table
        lstOfCDObjects = DataProcessor.delete_inventory(lstOfCDObjects,intIDDel)
        
        #Display remaining items in the list.
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    # 3.6 process save inventory to file
    elif strChoice == 's':
        
        #Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        
        print()
        
        #Process choice
        if strYesNo == 'y':
            
            #Calling the function to write Inventory details to a file
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            
        else:
            
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            
        continue  # start loop back at top.
        
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')