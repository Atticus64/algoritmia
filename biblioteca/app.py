from InquirerPy import prompt

"""
Aplicacion de Libreria Morelos
Features:
  - Listar libros
  - Buscar libro por nombre
  - Buscar libro por genero
"""
class Book:
  name: str = ""
  author: str = ""
  genre: str = ""
  year: int = 0

  def __init__(self, name: str, author: str, genre: str, year: int):
      self.name = name
      self.author = author
      self.year = year
      self.genre = genre
  
  def print(self):
      print(f"Nombre: {self.name}, Autor: {self.author}", end=" ")
      print(f"Genero: {self.genre}, Año: {self.year}")
       

def main():
  print("Libreria Morelos")
  books: list[Book] = [] 
  file = open("books.txt", encoding="utf8")
  for line in file.readlines():
      if len(line) == 0 or line.isspace():
          continue
      line = line.strip()
      line = line.split(",")
      name = line[0].strip()
      author = line[1].strip()
      year = int(line[2])
      genre = line[3].strip()
      books.append(Book(name, author, genre, year))

  options = ["" for i in range(3)]
  options[0] = "Listar libros"
  options[1] = "Buscar libro por nombre"
  options[2] = "Buscar libro por genero"
  questions = [
      {
          "type": "list",
          "message": "Que Tarea deseas realizar",
          "choices": [options[0], options[1], options[2], "Salir"], 
          "name": "choice"
      },
  ]

  result = prompt(questions)
  opt = result["choice"]
  do_command(opt, books)

def do_command(cmd: str, books: list[Book]):
  if cmd.startswith("Listar"):
    for book in books:
      book.print()
  elif cmd.startswith("Buscar libro por nombre"):
    res = prompt(
      [
       {
         "type": "input", 
         "message": "Cual es el nombre del libro:", 
         "name": "name"
       }
      ]
    )
    found = False
    for book in books:
      search: str = res["name"]
      if book.name.lower().find(search.lower()) != -1:
        book.print()
        found = True

    if not found:
      print("Libro no encontrado")
        
  elif cmd.startswith("Buscar libro por genero"):
    res = prompt(
      [
        {
          "type": "input", 
          "message": "Cual es el genero del libro:", 
          "name": "genre"
        }
      ]
    )
    found = False
    for book in books:
      genre = res["genre"]
      if book.genre.lower().find(genre.lower()) != -1:
        book.print()
        found = True
       
    if not found: 
      print("Libro no encontrado")

  elif cmd.startswith("Salir"):
    exit()

if __name__ == "__main__":
  main()
