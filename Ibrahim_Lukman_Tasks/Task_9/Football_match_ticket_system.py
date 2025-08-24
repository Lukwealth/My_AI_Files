

seat_numbers = set(range(1, 51))
print(seat_numbers)
bookings = []

book = int(input("Dear user, Kindly book a sit by entering a seat number: "))

if book in bookings:
    print(f"seat number {book} has been previously booked")

elif book not in bookings:
    print(f"You have successfully booked seat number {book}. Kindly have your seat")
    available_seat = seat_numbers.discard(book)
    print(f"Here are the available seats left..\n{available_seat}")

elif book < 1:
    print("You have entered a wrong input, kindly try again...")

elif book > 50:
    print("You have entered a wrong input, kindly try again...")