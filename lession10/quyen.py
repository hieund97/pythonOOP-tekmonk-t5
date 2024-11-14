import csv
import pandas

categ = input("Whadd'ya wanna search by? ")
monik = input("What's the name? ")

peeps = open("new.csv", "r")
exist = list(csv.reader(peeps))

peep = pandas.read_csv("new.csv")
peep_list = peep[categ].to_list()


if monik in peep_list:
        print(monik)
        print("".join(exist[peep_list.index(monik)+1]))