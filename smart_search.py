from googlesearch import search

query = input("Что ищем?Введи название аниме/трека")

print("Запускаю скрытый поиск в Google...")

results = search(query, num_results=1)
for url in results:
     print("Я нашел нужную ссылку!!!")
     print(url)
