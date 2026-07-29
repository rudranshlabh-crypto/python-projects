items=["pencil","eraser","sharpner","notebook"]
stock_count=[12, 0, 5, 20]

inventary={iten:count for item,count in zip(item,stock_count)}
print("full inventary", inventary)

in_stock_items=[item for item in items if inventary[item]>0]
print("in stock items are", in_stock_items)

choosenitem=input("which item you want to guide")
if choosenitem not in inventary or inventary [choosenitem]==0:
    print(choosenitem, "not present in inventary")
    exit()