from PIL import Image


run = True
while run:
    print("***************************************")
    print("На сколько процентов вы хотите изменить яркость:")
    delta = int(input())
    if not(delta <= 100 and delta >= -100):
        print("!!!ОШИБКА!!!")
        print("Вводимое число должно быть в пределе от -100% до 100%")
    else:
        delta = 1 + (delta / 100)
        run = False
        break
img = Image.open("photo.png")
pixels = img.load()
width, height = img.size
for column in range(width):
    for row in range(height):
        r = pixels[column, row][0]
        g = pixels[column, row][1]
        b = pixels[column, row][2]
        r = round(r * delta)
        g = round(g * delta)
        b = round(b * delta)
        pixels[column, row] = (r, g, b)
img.save("res.png")
print("Готово! :)")