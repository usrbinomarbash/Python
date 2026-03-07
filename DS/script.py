for i in range(100):
    with open('text' + str(i) + '.txt', 'w') as f:
        f.write(str(i))
