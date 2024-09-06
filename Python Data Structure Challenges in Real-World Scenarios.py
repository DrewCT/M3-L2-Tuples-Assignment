def add_book(library, new_book):
    if new_book in library:
        print(f"'{new_book[0]}' by {new_book[1]} already exists in the library.")
    else:
        library.append(new_book)
        print(f"'{new_book[0]}' by {new_book[1]} has been added to the library.")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

new_book1 = ("To Kill a Mockingbird", "Harper Lee")
new_book2 = ("1984", "George Orwell")  

add_book(library, new_book1)
add_book(library, new_book2)

print("\nUpdated Library:")
for book in library:
    print(f"Title: {book[0]}, Author: {book[1]}")