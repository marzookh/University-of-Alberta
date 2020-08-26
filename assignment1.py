#----------------------------------------------------
# Assignment 1
#
# Author: Marzookh
# Collaborators:
# References: https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
#----------------------------------------------------
def main():
    
    file1 = open('products.txt','r')
    items = file1.readlines()
    item = []
    item_code = []
    itemname_code = {}
    
    for i in range(len(items)):
        items[i]= items[i].strip()
        items[i] = items[i].split(';')
        item_code.append(items[i][0])
        item.append(items[i][1])
    
    # creating itemname and code dict
    itemname_code = dict(zip(item_code,item))

     
    file2 = open('suppliers.txt','r')
    suppliers = file2.readlines()
    phone_supplier = {}
    phone = []
    supplier = []
    
    for i in range(len(suppliers)):
        suppliers[i] = suppliers[i].strip()
        suppliers[i] = suppliers[i].split(';')
        phone.append(suppliers[i][0])
        supplier.append(suppliers[i][1])
        
    # creating supplier name and phone
    phone_supplier = dict(zip(phone,supplier))
    
    
    file3 = open('onshelves.txt','r')
    stocks = file3.readlines()
    stock = []#stock is the number of products to order
    stock_order = []
    for i in range(len(stocks)):
        stocks[i] = stocks[i].strip()
        stocks[i] = stocks[i].split('#')
        stock.append(int(stocks[i][1]))
    
    #checking inventory and subtracting from 50
    for i in range(len(stock)):
        if stock[i] < 20:
            stock[i] = 50 - stock[i]
            stock_order.append(stock[i])

    #joining stock needed and item_code in a dict
    stock_needed = dict(zip(item_code,stock_order))
     


    file4 = open('availability.txt','r')
    avail = file4.readlines()
    low = ''
    for i in range(len(avail)):
        avail[i] = avail[i].strip()
        avail[i] = avail[i].split(',')
    
    #checking similar product availability
    for i in range(len(avail)-2):
        if avail[i][0] == avail[i+1][0]:
            
            if float(avail[i][2]) > float(avail[i+1][2]):
                del avail[i]
            elif float(avail[i][2]) < float(avail[i+1][2]):
                del avail[i+1]
            else:
                del avail[i]


    #sorting the list with respect to suppliers numbers
    def Sort(sub_list): 
        '''sorts by specific element in list'''
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
        sub_list.sort(key = lambda x: x[1]) 
        return sub_list
    Sort(avail)
    
    item_supplier = {}
    supplier_items =[]
    supplier_phone = []
    cost = []
    #extracting items, phone numbers and cost from avail list
    for i in range(len(avail)):
        supplier_items.append(avail[i][0])
        supplier_phone.append(avail[i][1])
        cost.append(avail[i][2])
    
    # joining item_code and supplier phone
    item_supplier = dict(zip(supplier_items,supplier_phone))
    
    
    #creating a dict with item code and cost
    itemcodeAndcost = dict(zip(supplier_items,cost))

    #opening the file to write
    filee = open('orders.txt','w+')
    
    total_cost = 0
    highest_cost = 0
    highest_supplier = ''
    highest_supplier_no = ''

    #printing and writing headers
    filee.write('+--------------+------------------+--------+----------------+----------+\n')
    filee.write('| Product code | Product Name     |Quantity| Supplier       | Cost     |\n')
    filee.write('+--------------+------------------+--------+----------------+----------+\n')
    print('+--------------+------------------+--------+----------------+----------+')
    print('| Product code | Product Name     |Quantity| Supplier       | Cost     |')
    print('+--------------+------------------+--------+----------------+----------+')

    same = ''
    same_cost =''
    new_num = ''
    
    #loop for assigning values to variables
    for item_code in item_supplier.keys():
        if item_code in stock_needed.keys():
            cumalative_cost = 0
            Same = False
            star = False
            cost_same = False
            #product code = a
            a = item_code
            
            #quantity = c
            c = stock_needed[item_code]
            if int(c) > 40:
                star = True
            
            #product name = b
            b = itemname_code[item_code]#outputs product name for every item_code

            #adding the star for orders over 40 units
            if star:       
                b = '*' + b
            else:
                b = ' ' + b
                
            
            #supplier number = d
            if same == item_supplier[item_code]:
                cumalative_cost = same_cost
                new_num = same
                
            d = item_supplier[item_code] #outputs supplier_phone for every item_code in stock_needed
            same = d

            #calculating cost
            individual_cost = float(itemcodeAndcost[item_code])
            no_of_items = c
            total_cost_row = (individual_cost * no_of_items) 
            
            #row cost = e
            e = total_cost_row
            same_cost = e
            total_cost  = total_cost + total_cost_row
            filee.write('|{:^14}|{:<18.17}|{:>7d} | ({}) {} {} | ${:>7.2f} |\n'.format(a,b,c,d[:3],d[3:6],d[6:],e))
            print(('|{:^14}|{:<18.17}|{:>7d} | ({}) {} {} | ${:>7.2f} |'.format(a,b,c,d[:3],d[3:6],d[6:],e)))
            
            #checking to see if two suppliers have the same product
            if total_cost_row + cumalative_cost > highest_cost:
                
                highest_cost = total_cost_row + cumalative_cost
                highest_supplier = phone_supplier[d]
                new_num = d
            elif total_cost_row + cumalative_cost == highest_cost:
                cost_same = True
                
       
    filee.write('+--------------+------------------+--------+----------------+----------+\n')
    filee.write('| Total Cost   |                ${:>10.2f}|\n'.format(total_cost))
    filee.write('+--------------+---------------------------+\n')
    filee.write('Highest cost: {} ({}) {} {} [{}] \n'.format(highest_supplier,d[:3],d[3:6],d[6:],highest_cost))

    print('+--------------+------------------+--------+----------------+----------+')
    print('| Total Cost   |                ${:>10.2f}|'.format(total_cost))
    print('+--------------+---------------------------+')
    print('Highest cost: {} ({}) {} {} [{}] '.format(highest_supplier,new_num[:3],new_num[3:6],new_num[6:],highest_cost))
    if cost_same:
        print('Highest cost: {} ({}) {} {} [{}] '.format(highest_supplier,new_num[:3],new_num[3:6],new_num[6:],highest_cost))
    
    
main()










