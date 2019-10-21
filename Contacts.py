
class Contacts:

    def __init__(self):

        while True:
            try:
                print(
                    "--------------\nContacts:1   |\nAdd:2        |\nEdit:3       |\nDelete:4     |\nDial:5       "
                    "|\nExit:0       |\n--------------\n")

                value = int(input("Please choose and enter a number. What would you like to do? "))

                if value == 1:

                    self.short_list()

                    if len(contacts_short_list) != 0:
                        x = int(input("If you want to see detailed information of the contacts, please insert '9': "))
                        if x == 9:
                            self.full_list()


                elif value == 2:
                    self.getting_info()

                elif value == 3:
                    self.short_list()
                    if len(contacts_short_list) != 0:
                        edit_value = int(input("Please choose which contact do you want to edit.. : "))
                        self.edit_info(edit_value)

                elif value == 4:
                    self.short_list()

                    if len(contacts_short_list) != 0:
                        self.delete_number()

                elif value == 0:
                    break

            except ValueError:
                print("Please insert between 0 and 5")

    def edit_info(self, edit_value):

        while True:

            if (edit_value - 1) in range(0, len(contacts_full_list)):
                print("First Name: FN\nLast Name: LN\nAge: A\nGender: G\nNumber: NO\nCancel:0\n")
                result = input("Please enter short code of your request..")

                if result == 0:
                    break

                if result.upper() == "FN":
                    print("Previous value: " + contacts_full_list[edit_value - 1]["First Name:"])
                    f_n = input("First Name*:")
                    contacts_full_list[edit_value - 1]["First Name:"] = f_n

                if result.upper() == "LN":
                    print("Previous value: " + contacts_full_list[edit_value - 1]["Last Name:"])
                    l_n = input("Last Name*:")
                    contacts_full_list[0]["Last Name:"] = l_n

                if result.upper() == "A":
                    print("Previous value: " + contacts_full_list[edit_value - 1]["Age:"] )
                    age = input("Age:")
                    contacts_full_list[0]["Age:"] = age

                if result.upper() == "G":
                    print("Previous value: " + contacts_full_list[edit_value - 1]["Gender:"] )
                    gender = input("Gender (M/F):")
                    contacts_full_list[0]["Gender:"] = gender

                if result.upper() == "NO":

                    while True:
                        print("Previous value: " + contacts_full_list[edit_value - 1]["Number:"])
                        no = input("Number*:")
                        if len(no) == 10:
                            contacts_full_list[0]["Number:"] = no
                            break

                        print("Please insert a valid number without putting '0'")

                self.edit(edit_value, contacts_full_list[edit_value - 1]["First Name:"], contacts_full_list[edit_value - 1]["Last Name:"],
                    contacts_full_list[edit_value - 1]["Number:"], contacts_full_list[edit_value - 1]["Age:"],
                    contacts_full_list[edit_value - 1]["Gender:"])

                m = ["FN", "LN", "A", "G", "NO", ]

                if result.upper() in m:
                    print(str(edit_value) + ". contact has been edited..")

                end = input("Do you want to do anything else? (y/N)")
                if end.upper() != 'Y':
                    break


    def adding_list(self, short_info, detailed_info):

        contacts_short_list.append(short_info)
        contacts_full_list.append(detailed_info)

    def add_number(self, first_name, last_name, number, age=" ", gender=" "):

        detailed_info = {"First Name:": first_name.title(), "Last Name:": last_name.title(), "Number:": number,
                         "Age:": age,
                         "Gender:": gender.title()}

        short_info = first_name.title() + " " + last_name.title()
        print("\n" + first_name.title() + " " + last_name.title() + " has been "
                                                                    "created..\n----------------------------------\n")

        self.adding_list(short_info, detailed_info)
        return first_name, last_name, number, age, gender

    def delete_number(self):

        while True:
            try:
                delete_value = int(input("Please choose which contact do you want to delete..(Go previous page:0) : "))
                if delete_value == 0:
                    break

                elif (delete_value - 1) in range(0, len(contacts_full_list)):
                    print(str(contacts_short_list[delete_value - 1]) + " has been deleted from Contacts..")

                    dict1 = contacts_full_list[delete_value - 1]
                    if dict1 in contacts_full_list:
                        contacts_full_list.remove(dict1)

                    del contacts_short_list[delete_value - 1]
                    break

                else:
                    print("Please insert a valid contact..")

            except:
                print("Please insert a valid contact..")

    def edit(self, no, first_name, last_name, number, age=" ", gender=" "):

        contacts_full_list[no - 1] = {"First Name:": first_name.title(), "Last Name:": last_name.title(),
                                      "Number:": number,
                                      "Age:": age,
                                      "Gender:": gender.title()}

        contacts_short_list[no - 1] = first_name.title() + " " + last_name.title()

    def full_list(self):

        if len(contacts_full_list) == 0:
            print("\nIt seems there is no contacts here..")

        else:
            for i in range(len(contacts_full_list)):
                print("----------------------\n" + str(i + 1) + "  |\n----------------------")
                dict = contacts_full_list[i]
                for key, value in dict.items():
                    print(key + " " + value)
                print("\n")

    def short_list(self):

        if len(contacts_short_list) == 0:
            print("\nIt seems there is no contacts here..")

        else:
            sorted_list = sorted(contacts_short_list)
            for i in range(len(sorted_list)):

                print(str(i + 1) + ": " + sorted_list[i])
            print("\n")

        print("---- Total Number of Contacts:" + str(len(contacts_short_list)) + " ----\n")

    def getting_info(self):

        print("If you want to cancel, press '0'..")

        while True:
            while True:
                f_n = input("First Name*:")
                if len(f_n) > 0:
                    break
                else:
                    print("It is a mandatory place. Please enter your name..")

            if f_n == '0':
                break

            while True:
                l_n = input("Last Name*:")
                if len(l_n) > 0:
                    break
                else:
                    print("It is a mandatory place. Please enter your surname..")

            if l_n == '0':
                break

            while True:
                number = input("Number*:")
                if len(number) == 10 or number == '0':
                    break
                else:
                    print("Please insert a valid '10-digit' number without putting '0'")

            if number == '0':
                break

            while True:
                try:
                    age = int(input("Age:"))
                    if age > 0 and age < 105:
                        break
                    else:
                        print("The normal human's ages should be between '1' and '105'")
                except ValueError:
                    print("Please insert a value between '0' and '105'")

            if age == 0:
                break

            while True:
                gender = input("Gender (M/F):")
                if gender.upper() == "M" or gender.upper() == "F":
                    break
                else:
                    print("Please enter 'M' or 'F'..")

            if gender == '0':
                break

            self.add_number(f_n, l_n, number, str(age), gender)
            break


    def favorites(self):

        """Codes will be here"""

    def recent(self):

        """Codes will be here"""


contacts_full_list = []
contacts_short_list = []
Contacts()
