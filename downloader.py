import requests

links = [
    "https://authorkyleatwood.wordpress.com/wp-content/uploads/2021/07/guts-a-berserk-character-analysis.png?w=640",
    "https://justbuildthings.com/images/anime-characters/guts.png",
    "https://static0.cbrimages.com/wordpress/wp-content/uploads/2023/01/berserk-brand.jpg?w=1200&h=675&fit=crop"
]

print("Запуск массового скачивания")

for i, url in enumerate(links, start=1):
    print(f"Качаю файл№{i}...")

    response = requests.get(url)

    filename = f"pic_{i}.png"

    with open(filename, "wb") as file:
        file.write(response.content)

print("Все файлы успешно скачаны и пронумерованы!!!")
