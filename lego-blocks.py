def legoBlocks(n, m):
    layer_one = [1,2,4,8]
    for i in range(4, m):
        layer_one.append(sum(layer_one[-4:]))

    total_com = layer_one[-1] ** n
    solid = [1]
    for width in range(1, m):
        total_com -= solid[-1] * layer_one[m-width] ** m
        solid.append(layer_one)

legoBlocks(1, 5)