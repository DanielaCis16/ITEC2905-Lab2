class Author:
    def __init__(self, name):
        self.name = name
        self.books = []  # start with no books

    def publish(self, title):
        if title in self.books:
            print(f"Error: '{title}' is already published by {self.name}.")
        else:
            self.books.append(title)

    def __str__(self):
        return f"{self.name}, Books: {', '.join(self.books)}"


def main():
    ggm = Author("Gabriel García Márquez")
    ggm.publish("One Hundred Years of Solitude")
    ggm.publish("Love in the Time of Cholera")
    print(ggm)

    jkr = Author("J.K. Rowling")
    jkr.publish("Harry Potter and the Philosopher's Stone")
    jkr.publish("Harry Potter and the Chamber of Secrets")
    print(jkr)


main()
