import matplotlib.pyplot as plt


def flood_fill(arr_numbers, x, y):
    if x < 0 or y < 0 or x == arr_numbers.shape[0] or y == arr_numbers.shape[1]:
        return arr_numbers
    if arr_numbers[x, y] == 0 or arr_numbers[x, y] == 2:
        return arr_numbers

    plt.imshow(arr_numbers, cmap="gray")
    plt.show(block=False)
    plt.pause(0.02)
    plt.clf()

    arr_numbers[x, y] = 2
    arr_numbers = flood_fill(arr_numbers, x + 1, y)
    arr_numbers = flood_fill(arr_numbers, x - 1, y)
    arr_numbers = flood_fill(arr_numbers, x, y + 1)
    arr_numbers = flood_fill(arr_numbers, x, y - 1)
    return arr_numbers


def main():
    # img = plt.imread("files/img0.png")[:, :, 0]
    img = plt.imread("files/img1.png")[:, :, 0]
    #img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
