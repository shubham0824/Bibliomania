# listofbooks = {'Python':
#     {
#         'isbn':'1-7632-834',
#         'author':'a'
#     },
#     'C++':
#     {
#         'isbn':'1-49857-2543',
#         'author':'b'
#     },
#     'Java':
#     {
#         'isbn':'2-48573-345790',
#         'author':'c'
#     },
#     'Javascript':
#     {
#         'isbn':'2-55353095-305',
#         'author':'d'
#     },
#     'Django':
#     {
#         'isbn':'2-35457-25895',
#         'author':'e'
#     },
#     'Flask':
#     {
#         'isbn':'2-386734-2353453',
#         'author':'f'
#     },
#     'Flutter':
#     {
#         'isbn':'2-4398734-58498734',
#         'author':'g'
#     },
#     'Kotlin':
#     {
#         'isbn':'2-59873653-983534',
#         'author':'h'
#     },
#     'React':
#     {
#         'isbn':'9-4587634-34975634',
#         'author':'i'
#     },
#     'Angular':
#     {
#         'isbn':'32-987637-985345',
#         'author':'j'
#     },
#     'Nodejs':
#     {
#         'isbn':'2-4357634578-59348',
#         'author':'k'
#     },
#     'Mongodb':
#     {
#         'isbn':'3-8327650-87534',
#         'author':'l'
#     },
#     'Vuejs':
#     {
#         'isbn':'2-43875-59834567',
#         'author':'m'
#     },
# }




import requests

# # r2 = requests.get('https://www.googleapis.com/books/v1/volumes?q=python&printType=books&key=AIzaSyD7Ja_vRi7qH1_F2iLn-GZv3nc_f0O2vdc')

# # r2_json = r2.json()
# # for i in range(len(r2_json['items'])):
# #     print(r2_json['items'][i]['volumeInfo']['title'])



# r1 = requests.get('https://www.googleapis.com/books/v1/volumes?q=""+inauthor:"Dan+bader"&key=AIzaSyD7Ja_vRi7qH1_F2iLn-GZv3nc_f0O2vdc')

# print(r1.text)

# r1_json = r1.json()
# author_name = 'kd'
# print(f"All books that are written by {author_name}:-\n")
# for i in range(len(r1_json['items'])):
#     print(r1_json['items'][i]['volumeInfo']['title'])




# r3 = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=""+isbn:9781775093305&key=AIzaSyD7Ja_vRi7qH1_F2iLn-GZv3nc_f0O2vdc')

# r3_json = r3.json()
# print(r3.text)

# print(f"Book Name: {r3_json['items'][0]['volumeInfo']['title']}")
# print(f"ISBN: {r3_json['items'][0]['volumeInfo']['industryIdentifiers'][1]['identifier']}")
# for i in range(len(r3_json['items'][0]['volumeInfo']['authors'])):
#     print(f"Authors Name: {r3_json['items'][0]['volumeInfo']['authors'][i]}")