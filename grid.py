
def product(*args, repeat=3):
# product(range(2), repeat=3) --> (0,1) выход [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]
    # *args распаковать объект внутри которого находятся элементы (в этом случае range(2))
    pools = [tuple(pool) for pool in args] * repeat
    # pool=(0,1)
    # pool * 3 --> pools ((0,1,0,1,0,1))
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
        # выражение генеротора [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]
        # y = число  проходит все элементы в pool
        # x = лист проходит все элементы из result
        # x+[y] = на каждой итерации добавляем элемент y в лист x складываем в массив result

    for prod in result:
        yield prod
    # складывает элементы в result prod генератор возвращает список элементов на подобие [1,0,1]


# cubic
def make_grid(points, spacing, spacing1=None, spacing2=None):
    grid = [[]]
    grid.clear()
    if(spacing1 == None):
        spacing1 = spacing
    if(spacing2 == None):
        spacing2 = spacing
    for i in product(range(points), repeat=3):
        grid.append(i)
        # заполнение grid
    for i in range(points ** 3):
        grid[i][0] = (grid[i][0] - int(points / 2)) * spacing
        grid[i][1] = (grid[i][1] - int(points / 2)) * spacing1
        grid[i][2] = (grid[i][2] - int(points / 2)) * spacing2

        # домножение элементов grid на размерный коэффициент
    return grid


def v_grid(points, spacing,spacing1=None,spacing2=None):
    grid = make_grid(points,spacing,spacing1,spacing2)
    grid1 = [[]]
    grid1.clear()
    if (spacing1 == None):
        spacing1 = spacing
    if (spacing2 == None):
        spacing2 = spacing

    for i in product(range(points-1), repeat=3):
        grid1.append(i)
    for i in range((points-1) ** 3):
        grid1[i][0] = (grid1[i][0] - int(points / 2) + 0.5) * spacing
        grid1[i][1] = (grid1[i][1] - int(points / 2) + 0.5) * spacing1
        grid1[i][2] = (grid1[i][2] - int(points / 2) + 0.5) * spacing2
    return grid+grid1


def g_grid(points, spacing,spacing1=None,spacing2=None):
    grid = make_grid(points, spacing,spacing1,spacing2)
    grid1 = [[]]
    grid1.clear()
    grid2 = [[]]
    grid2.clear()
    grid3 = [[]]
    grid3.clear()
    if (spacing1 == None):
        spacing1 = spacing

    if (spacing2 == None):
        spacing2 = spacing

    for i in product((range(points -1)), repeat=3):
        grid1.append(i)
    for i in product(range((points -1)), repeat=3):
        grid2.append(i)
    for i in product(range((points -1)), repeat=3):
        grid3.append(i)

    for i in range((points -1) ** 3):

        grid1[i][0] = (grid1[i][0] - int(points / 2) + 0.5)
        grid1[i][1] = (grid1[i][1] - int(points / 2) + 0.5)
        grid1[i][2] = (grid1[i][2] - int(points / 2))
        grid1.append([(grid1[i][0] - int(points / 2) + 1),
                      (grid1[i][1] - int(points / 2) + 1), (grid1[i][2] - int(points/2) + 2)])

        grid2[i][0] = (grid2[i][0] - int(points / 2) + 0.5)
        grid2[i][1] = (grid2[i][1] - int(points / 2))
        grid2[i][2] = (grid2[i][2] - int(points / 2) + 0.5)
        grid2.append([(grid2[i][0] - int(points / 2) + 1.5),
                      (grid2[i][1] - int(points / 2) + 1.5), (grid2[i][2] - int(points / 2) + 1)])

        grid3[i][0] = (grid3[i][0] - int(points / 2))
        grid3[i][1] = (grid3[i][1] - int(points / 2) + 0.5)
        grid3[i][2] = (grid3[i][2] - int(points / 2) + 0.5)
        grid3.append([(grid3[i][0] - int(points / 2) + 1.5),
                      (grid3[i][1] - int(points / 2) + 1.5),(grid3[i][2] - int(points / 2) + 1)])

    ans = grid1 + grid2 + grid3
    for el in ans:
        el[0] = el[0] * spacing
        el[1] = el[1] * spacing1
        el[2] = el[2] * spacing2
    return ans + grid

