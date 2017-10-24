goods = [20, 10, 5, 5, 3, 2, 20, 10]
goods_name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
n = len(goods)  # Number (Max) of goods


def lookInSack(sack, max_index):
    global goods, goods_name
    print('You Buy :', end=' ')
    # Compare Index between goods and goods' name #
    for i in range(max_index + 1):
        if sack[i] is not None:
            print(str(goods_name[sack[i]]) + '(' + str((goods[sack[i]])) + ')', end=' ')
    print()


def shopping(sack, i_sack, money, i_goods):
    if i_goods < n:
        # Start from 0
        # start at a >> finish >> start at b >> ... >> start at h >> finish
        price = goods[i_goods]
        # Assign goods'price
        if money < price:
            # Cannot Buy >> Go next Goods
            shopping(sack, i_sack, money, i_goods + 1)
        else:
            # Can Buy >> Pay Money + Pick up item
            money -= price
            sack[i_sack] = i_goods
            if money == 0:
                # Check >> No Money >> Look In
                lookInSack(sack, i_sack)
            else:
                # Check >> There is Money Left >> Go next Goods
                shopping(sack, i_sack + 1, money, i_goods + 1)
            shopping(sack, i_sack, money + price, i_goods + 1)


money = 20
i_goods = 0
sack = n * [None]
i_sack = 0
shopping(sack, i_sack, money, i_goods)
