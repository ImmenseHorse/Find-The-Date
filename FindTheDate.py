#This program was written by Duc Nguyen on Nov 20, 2019.
#This program tests the three functions IsLeapYear(year),IsValidDate(date),DayOfTheYear(date)
#and determines if they are robust or not.

import UsefulDates

def main():
    YEARS = [4, 6, 96, 300, 1056, 1500, 567, 1600, 2001, 10230, 123.5, -1]
    #YEARS - the list of years to test the IsLeapYear() function
    
    for x in range(len(YEARS)):
        #Determine if the year is a leap year
        if UsefulDates.IsLeapYear(YEARS[x]) == True:
            print("The year",YEARS[x],"is a leap year")
        else:
            print("The year",YEARS[x],"is not a leap year")
            
    print()
    DATES = ["02/-123/2001", "/ /", "02/29/2012", "Feb/first/nineteen twenty", " ", "1/1/1", "02/-2/2002", "@#$%#01/03/1975"]
    #DATES - the list of dates to test the IsValidDate() function

    for x in range(len(DATES)):
        #Determine if the date is a valid date
        if UsefulDates.IsValidDate(DATES[x]) == True:
            print(DATES[x],"is a valid date")
        else:
            print(DATES[x],"is not a valid date")
            
    print()
    MORE_DATES = ["03/01/2011", "12/31/2011", "March/1/1234", "41/second/45678", "03/01/2000"]
    #MORE_DATES - the list of dates to test the DayOfTheYear() function
    
    #Determine the day of the year of a date
    for x in range(len(MORE_DATES)):
        print(MORE_DATES[x],"is day number",UsefulDates.DayOfTheYear(MORE_DATES[x]))

main()
