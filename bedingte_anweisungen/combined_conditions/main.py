# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = (discounted == True) or (lowStock != False)
promotion = (discounted == False) and (not lowStock )
print ("Is the item eligible for promotion?", promotion)
