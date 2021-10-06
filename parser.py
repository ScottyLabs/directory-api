import search

result = search.advanced("Gael")

# print(soup.find('h1', id="listing").text)
print(result.h1.text)
info = result.p.contents
print(info[1][1:])
print(info[4][1:])
print(info[7][1:])
print(info[11].text)
