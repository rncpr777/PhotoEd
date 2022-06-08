from PIL import Image


print("*********************")
print("Выберите соотношение:")
print("1. 16:10")
print("2. 16:9")
print("3. 5:4")
print("4. 4:3")
print("5. 3:4")
print("6. 1:1")
print("7. Не менять")
soot = int(input())
print("******************************************")
print("Вы хотите сделать изображение черно-белым?")
chb = bool(input())
img = Image.open("photo.png")
pixels = img.load()
width, height = img.size
if soot == 1:
    delen = width // 16
    width = delen * 16
    height = delen * 10
    img = img.resize((width, height))
elif soot == 2:
    delen = width // 16
    width = delen * 16
    height = delen * 9
    img = img.resize((width, height))
elif soot == 3:
    delen = width // 5
    width = delen * 5
    height = delen * 4
    img = img.resize((width, height))
elif soot == 4:
    delen = width // 4
    width = delen * 4
    height = delen * 3
    img = img.resize((width, height))
elif soot == 5:
    delen = height // 4
    width = delen * 3
    height = delen * 4
    img = img.resize((width, height))
elif soot == 6:
    height = width
    img = img.resize((width, height))
if chb == True:
    img = img.convert("L")
img.save("res.png")
print("Готово! :)")