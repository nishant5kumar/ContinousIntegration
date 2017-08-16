#-----------------------------------------------------------
#-----------------------------------------------------------
#-------------@Author: nishant.kumar_3@philips.com----------
#-----------------------------------------------------------
#-----------------------------------------------------------

import openpyxl

class xl():
    def xl_Parse(self):
        try:
            wb = openpyxl.load_workbook('framework.xlsx')
            sheet = wb.get_sheet_by_name('Sheet1')
            i = 2
            #print(sheet['B'+str(i)].value)
            while (str(sheet['B'+str(i)].value) != "None"):
                #print(sheet['B'+str(i)].value)
                i = i+1
            count = i-2
            lis = [[] for x in range(count)]
            #print (lis)
            for num in range(0,count):
                #print ("****",num)
                #This list needs to be appended for each column addition in XL sheet
                lis[num].append(sheet['B'+str(num+2)].value)
                lis[num].append(sheet['C'+str(num+2)].value)
                lis[num].append(sheet['D'+str(num+2)].value)
                lis[num].append(sheet['E'+str(num+2)].value)
                lis[num].append(sheet['F'+str(num+2)].value)
                lis[num].append(sheet['G'+str(num+2)].value)
            #print(lis)
            #for each in range(count):
                #print(each)
                #print(lis[each])
                              
            return count, lis
        except exception as e:
            print (e)
'''
if __name__== "__main__":
    count, lis = xl_Parse()
    print("----------",count)
    print("---------->",lis)
    
'''
