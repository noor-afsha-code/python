article_names = {
    "golden banana": 350,
    "flour": 200,
    "moon lit melon": 300,
    "sea weed bread": 205,
    "disco pie": 115,
    "silver apple": 145,
    "cactus": 50,
    "banana": 65}


#Giving the users information about the items

print("Available Articles")

#assigning tags to key (article), value (price), using dictionary_name.item()

for article, price in article_names.items():    
    print(f"{article.title()}: £{price}")

#giving options to exit or enter unlisted item
print("Type 'exit' to quit")
print("Item not on the list: type 'none'")

while True:

    #PromptfFor user to input the article's name with strip() and .lower() to make the input case and space insensitive
    article = input("Enter the article name: ").strip().lower()

    if article == 'exit':
        print("Thanks for shopping:)")
        break # loop will break here if user decides to exit

    elif article == 'none':
        #prompt for user to enter the item and its price
        item = input("Enter the name of the item: ").lower()
        price_tag = float(input ("Enter the price of the item: "))
        
        #calculating discount
        if price_tag >= 200:
           discount = price_tag * 10/100
        elif 100<= price_tag <=199.99:
            discount = price_tag * 5/100        
        else:
            discount = 0
        #calculation total cost
        total_cost = price_tag - discount

        print(f"Item: {item.title()}\n Discount: £{discount:}\n Total Cost: £{total_cost}")
        continue
    
    #retrieve the value of the article if the inout is an item from the dictionary using .get(key)
    price = article_names.get(article)

    #if the article doesn't meet any choice
    #prompt for the user to input again

    if price==None:
        print(f"Sorry!! {article.title()} does'nt exist. \n Try Again!!")
        continue #the loop will reach to the top of the loop and start again

    #calculating discount if the item is in the list
    elif price >= 200:
        discount = price * 10/100
           
    elif 100 <= price <= 199.99:
        discount = price * 5/100
       
    else:
        discount = 0
#calculating the cost of thei= item after the discount
    cost = price - discount
    
    print(f"Item:{article.title()}\n Discount: £{discount}\n  Total cost: £{cost}")


