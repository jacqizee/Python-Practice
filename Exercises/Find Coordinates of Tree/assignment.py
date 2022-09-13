def label_nodes(node, x=0, y=0):
    node.x = x
    node.y = y

    print((node.x, node.y), end=' ')

    counter = 0
    for child in node.children:
        counter_increment = label_nodes(child, node.x + 1, node.y + counter)
        if counter_increment:
            counter += counter_increment
        else:
            counter += 1

    return counter