import os
import logging as lg
import sqlite3
import csv

lg.basicConfig(filename="bag_of_words.log", level=lg.INFO,
               format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# create handlers
console_log = lg.StreamHandler()
console_log.setLevel(lg.INFO)
format = lg.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_log.setFormatter(format)

# create custom logger
lg.getLogger("").addHandler(console_log)
logger = lg.getLogger("txt_op")
logger1 = lg.getLogger("countWord")
logger2 = lg.getLogger("StartingAlphaCount")
logger3 = lg.getLogger("fiterWords")
logger4 = lg.getLogger("Zip_DBcreate_store")
logger5 = lg.getLogger("fetch_db_data")

class txtop:

    def __init__(self):
        """
        Dynamically takes user inputs when class instance is created, checks if it's a .txt file/filepath
        """
        self.Variabledt = {}
        # self.__nottxtFlag = 0
        self.__flag = True

        while self.__flag:
            self.__nottxtFlag = 0  # nottxt flag
            try:
                self.number_files = int(input("Enter the number of txt files : "))
                for i in range(1, self.number_files + 1):
                    self.Variabledt["file" + str(i)] = input(f"Enter No.{i} Filename/path with ext : ")
                    self.istxt(self.Variabledt["file" + str(i)])
                    if self.__nottxtFlag == 1:
                        print("if executing even when there is an exception !!!!!")
                        break
                else:
                    self.__flag = False
                continue
            except Exception as e:
                logger.error(str(e))
                continue

    def istxt(self, file):
        """
        Checks if the file passed is a .txt file

        :param file: file or file path
        :return: TRUE in case if it's a .txt file, else raise a custom exception

        """
        if not file.endswith(".txt") or not os.path.isfile(file):
            self.__nottxtFlag = 1
            raise Exception(file, " is not a .txt file. Please Enter input files again !")
        return 1

    def countWord(self):
        """
        Counts the number of words in a given input file key, which was created with the constructor
        :return: Creates a list of tuple of words with it's count and dumps this data in a file

        """
        logger1.info("======== countWord function START =============")
        while True:
            try:
                logger1.info(f"Choose the file Key from files input dictionary : {self.Variabledt}")
                filename = self.Variabledt[input("Please Enter the file Key here : ")]
                f = open(filename, "r+", encoding="utf8")
                f.seek(0)
                data = csv.reader(f)
                alpha_lst = []
                for line in data:
                    alpha_str = ""
                    for ele in line[0].strip():
                        if ele.isalpha():
                            alpha_str = alpha_str + ele
                    alpha_lst.append(alpha_str)

                word_countlst = list(set([(word, alpha_lst.count(word)) for word in alpha_lst]))

                # open and write the word_countlst in a file
                with open("word_count.txt", "w") as f:
                    f.write("Word Count in file : " + filename)
                    f.write("\n")
                    f.write(str(word_countlst))
                    logger1.info(f"Please check word_count.txt file for word counts of {filename}")
                break

            except Exception as e:
                logger1.error(str(e))
                logger1.info("Invalid Input !! Please enter valid filename")
                continue

    def StartingAlphaCount(self):
        """
        Counts the number of starting alphabets in a given input file key, which was created with the constructor
        :return: Creates a list of tuple of starting alphabets with it's count and dumps this data in a file

        """
        logger2.info("======== StartingAlphaCount function START =============")
        eng_alpha = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
        eng_alphalst = eng_alpha.split(",")

        while True:
            try:
                logger2.info(f"Choose the file Key from files input dictionary : {self.Variabledt}")
                filename = self.Variabledt[input("Please Enter the file Key here : ")]
                f = open(filename, "r+", encoding="utf8")
                data = csv.reader(f)
                startAlphaCount_lst = []

                for ele in eng_alphalst:
                    f.seek(0)
                    counter = 0
                    for line in data:
                        if line[0].strip().startswith(ele):
                            counter += 1

                    startAlphaCount_lst += [(ele, counter)]

                # open and write startAlphacount_lst in a file

                with open("startAlphaCount.txt", "w") as f:
                    f.write("Alphabet Count in file " + filename)
                    f.write("\n")
                    f.write(str(startAlphaCount_lst))
                    logger2.info(f"Please check startAlphaCount.txt file for starting Alphabet counts of {filename}")
                break

            except Exception as e:
                logger2.info(str(e))
                logger2.info("Invalid Input !! Please enter valid filename")
                continue

    def fiterWords(self):
        """
        Filters just the words from a given input file key, which was created with the constructor
        :return: Creates a list of words and dumps this data in a file

        """
        logger3.info("======== fiterWords function START =============")
        while True:
            try:
                logger3.info(f"Choose the file Key from files input dictionary : {self.Variabledt}")
                filename = self.Variabledt[input("Please Enter the file Key here : ")]
                f = open(filename, "r+", encoding="utf8")
                f.seek(0)
                data = csv.reader(f)
                alpha_lst = []
                for line in data:
                    alpha_str = ""
                    for ele in line[0].strip():
                        if ele.isalpha():
                            alpha_str = alpha_str + ele
                    alpha_lst.append(alpha_str)

                alpha_lst = list(set(alpha_lst))

                # open and write alpha_lst to a file
                with open("filtered_words.txt", "w") as f:
                    f.write("filtered words in file " + filename)
                    f.write("\n")
                    f.write(str(alpha_lst))
                    logger3.info(f"Please check filtered_words.txt file for filtered out words of {filename}")
                break

            except Exception as e:
                logger3.error(str(e))
                logger3.info("Invalid Input !! Please enter valid filename")
                continue

    def DBTablecreate(self):
        """
        Create a DB and a Table
        :return:
        """
        logger4.info("======== Zip_DBcreate_store function START =============")
        try:
            # Establish the connection
            mydb = sqlite3.connect("bag_of_words.db")
            logger4.info("================ Connection Established ===================")

            cursor = mydb.cursor()
            logger4.info("================ Cursor Created ===================")

            cursor.execute("CREATE TABLE IF NOT EXISTS words (file1txt text,file2txt text,file3txt text,file4txt text, file5txt text);")
            logger4.info("================ Table Created ===================")

        except Exception as e:
            logger4.error(str(e))
        finally :
            mydb.close()
            logger4.info("DB closed")

    def Zip_store(self):
        """
        Zip and store the files data in to an DB created.

        """
        logger4.info("======== Zip_DBcreate_store function START =============")
        try:
            zipin_dict = {}

            for key, filename in self.Variabledt.items():
                f = open(filename, "r+", encoding="utf8")
                f.seek(0)
                zipin_dict[key + "_lst"] = []
                file_lst = f.readlines()
                for i in range(0, len(file_lst) - 1):
                    zipin_dict[key + "_lst"].append(file_lst[i][:-1])  # excluding \n from the string
                zipin_dict[key + "_lst"].append(file_lst[-1])
                f.close()

            mydb = sqlite3.connect("bag_of_words.db")
            cur = mydb.cursor()

            # print(zipin_dict)
            logger4.info("================ Starting to insert Values ===================")
            for data in zip(*zipin_dict.values()):  # * for undoing one level of list in dict.values()
                # print(data)
                query = f"INSERT INTO words values{tuple(data)}"
                print(query)
                cur.execute(query)
        except Exception as e:
            logger4.error("Thissssssss!!!!" + str(e))
        finally :
            mydb.close()
            logger4.info("DB closed")

    def fetch_db_data(self):
        """
        Fetch limited number of the records from the db

        """
        logger5.info("======== fetch_db_data function START =============")

        try:
            mydb = sqlite3.connect("bag_of_words.db")

            limit_number = int(input("Enter the number of records you want to fetch : "))

            cursor = mydb.cursor()
            cursor.execute(f"SELECT * FROM words LIMIT {limit_number};")

            for data in cursor.fetchall():
                print(data)

        except Exception as e:
            logger5.error(str(e))
        finally:
            mydb.close()
            logger5.info("DB closed")
