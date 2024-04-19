class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall):
        """This method add hall"""
        self._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, row, col, hall_no) -> None:
        super().__init__()
        self.__seats = {"row": row+1, "col": col+1}
        self.__show_list = []  # list of tuple
        self.__rows = row
        self.__cols = col
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        """This method make entries for movie"""
        available_seats = [
            [0 for i in range(self.__cols+1)] for j in range(self.__rows+1)]
        self.__show_list.append((int(id), movie_name, time, available_seats))

    def book_seats(self, movie_id, seat_row_no, seat_col_no):
        """This method book seats for a movie with given id and seat numbers"""
        for movie in self.__show_list:
            if movie_id in movie:
                if seat_col_no <= self.__cols and seat_row_no <= self.__rows:
                    if movie[3][seat_row_no][seat_col_no] == 0:
                        movie[3][seat_row_no][seat_col_no] = 1
                        return [True, """Seat booked"""]
                    else:
                        return [False, """Seat is already Booked"""]
                else:
                    return [False, """Invalid seat number"""]
        return [False, f"""Movie with {movie_id} id doesn't exist"""]

    def view_show_list(self):
        """"This method show the all available running movies"""
        for show in self.__show_list:
            print(f"""Movie name: {show[1]}. Movie id: {
                  show[0]}. Show Time: {show[2]}   """)

    def view_available_seats(self, id):
        """This method shows the available seats for the given id"""
        for show in self.__show_list:
            if id in show:
                seats = show[3]
                for i in range(self.__rows+1):
                    for j in range(self.__cols+1):
                        if seats[i][j] == 0:
                            print(f"""Empty Seat ({i},{j})""")
                return
        print(f"""No show with id {id} is available""")


obj = Hall(5, 5, 1)
obj.entry_show(1, "Iron man", "10 A.M.")
obj.entry_show(2, "Avengers: Endgame", "1 P.M.")
obj.entry_show(3, "Godzilla x Kong: The New Empire", "5 P.M.")


print("<--------Welcome to star cineplex -------->")
while True:
    try:
        print("Please select an option: ")
        print("1. View all running shows")
        print("2. View available seats")
        print("3. Book a ticket")
        print("4. Exit (Type 4 or any digit to exit)")
        cmd = int(input())
        if cmd == 1:
            print()
            print("<-------- Running Shows -------->")
            obj.view_show_list()
            print()
        elif cmd == 2:
            print()
            id = int(
                input("""\tPlease enter movie ID to check it's available seat: """))
            print("\t<---Available seats--->")
            obj.view_available_seats(id)
            print()
        elif cmd == 3:
            print()
            movieId = int(input("\tPlease enter Movie ID: "))
            rowNo = int(input("\tPlease enter seat ROW no: "))
            colNo = int(input("\tPlease enter seat COLUMN no: "))
            result = obj.book_seats(movieId, rowNo, colNo)
            if result[0]:
                print(f"""\tSeat booked successfully at: {rowNo, colNo}""")
            else:
                print(f"""Failed to book seat. Because {result[1]}""")
            print()
        else:
            break
    except:
        print("Unexpected error")
