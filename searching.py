#Binary Search
L = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
itemToSearchFor = 93
#find the midPoint (position)
startPos = 0
endPos = len(L)-1
midPoint = endPos // 2
found = False
while not found:
    #get the item at that position
    item = L[midPoint]
    #check if it's equal to the number you're searching
    if itemToSearchFor == item:
        #if it is then great print out the item
        found = True
        print (midPoint)
    else:
        #if it's not, we ask is the searchItem greater than the item or not
        if itemToSearchFor > item:
            #if the search item is greater, get "new" start point and use this to 
#slice list.
            startPos = midPoint + 1
        else:
            #if the search item is less, get the "new" end point and use this to 
#slice the list.
            endPos = midPoint - 1
        
        #then get the new mid point - repeat - while
        print (midPoint)
        midPoint = (startPos + endPos) // 2
    #print (item)