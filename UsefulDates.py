#This program was written by Duc Nguyen on Nov 18, 2019.
#This program dislays three (robust) functions which would be useful in any
#application that involved dates.

def IsLeapYear(year):
    """This function determines if the year is a leap year.
    Input: year as any number
    Output: True if it is a leap year
            False if it is not a leap year"""
    #year - the entered year by the user, which can be any number

    #Determine if the entered year is a number
    if str(year).isdigit():
        #Determine if the year is divisible by 4
        if year % 4 == 0:
            #Determine if the year is a century year
            if year % 100 != 0 :
                return True
            else:
                #Determine if the year is a century leap year
                if year % 400 == 0 :
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False

def IsValidDate(date):
    """This function determines if the date is a valid date.
    Input: date as any string
    Output: True if it is a valid date
            False if it is not a valid date"""
    #date - the entered date by the user, which can be any string
    
    #Determine if the date is in the proper format
    if len(date) == 10:
        #Dtermine the month of the date
        if int(date[:2]) == 1 or int(date[:2]) == 3 or int(date[:2]) == 5 or int(date[:2]) == 7 or int(date[:2]) == 8 or int(date[:2]) == 10 or int(date[:2]) == 12:
            if int(date[3:5]) <= 31:
                return True
            else:
                return False
        elif int(date[:2]) == 4 or int(date[:2]) == 6 or int(date[:2]) == 9 or int(date[:2]) == 11:
            if int(date[3:5]) <= 30:
                return True
            else:
                return False
        elif int(date[:2]) == 2:
            #Determine if the year is a leap year
            if IsLeapYear(int(date[6:])) == True:
                if int(date[3:5]) <= 29:
                    return True
                else:
                    return False
            else:
                if int(date[3:5]) <= 28:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False

def DayOfTheYear(date):
    """This function determines the day of the year of a date.
    Input: date as any string
    Output: A number from 1 to 365 or 366 if the date is valid
            –1 if the date is not valid"""
    #date - the entered date by the user, which can be any string
    #month - the month of the entered date
    #day - the day of the entered date
    #year - the year of the entered date
    #dayNum - the day of the year

    #Determine if the date is a valid date
    if IsValidDate(date) == True:
        month = int(date[:2])
        day = int(date[3:5]) 
        year = int(date[6:])
        #Simulate the situation when the month is either January or February
        if month <= 2:
            dayNum = 31*(month - 1) + day
        #Simulate the situation when the month is after February
        else:
            if IsLeapYear(year) == True:
                dayNum = 31*(month-1)+day - (4*month +23)//10 +1
            else: 
                dayNum = 31*(month-1)+day - (4*month +23)//10 
    else:
        dayNum = -1
    return dayNum
                
            
            
        
        
        
    
    

        
                    
                
                
        
        
    
    
    
        
                
                
                
        
        
        
