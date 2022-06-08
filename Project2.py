from PIL import Image


print("*********************")
print("Выберите соотношение:")
print("1. 16:9")
print("2. 4:3")
print("3. 1:1")
soot = int(input())
print("Вы хотите сделать изображение черно-белым?")
chb = bool(input())
img = Image.open("photo.png")
pixels = img.load()
width, height = img.size
if soot == 1:
    delen = width // 16
    width = delen * 16
    height = delen * 9
    img = img.resize((width, height))
img.save("res.png")
print("Готово! :)")