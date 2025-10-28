class Library:
  def book_info(self, title, author):
    return f"Title: {title}, Author: {author}"
class student(Library):
  def student_info(self, name, student_id):
    return f"Name: {name}, Student ID: {student_id}"
class libstu_info(student,Library):
    def full_info(self, title, author, name, student_id):
        book_details = self.book_info(title, author)
        student_details = self.student_info(name, student_id)
        return f"{book_details}\n{student_details}"
libstu = libstu_info()
print(libstu.full_info("Hacked", "George Orwell", "Rajbir singh", "2439052"))
