# Football Match

seat_numbers = set(range(1, 51))
bookings = []

try:
    book = int(input("Dear user, kindly book a seat by entering a seat number (1 - 50): "))

    if book < 1 or book > 50:
        print("You have entered a wrong input, kindly try again...")

    elif book in bookings:
        print(f"Seat number {book} has already been booked.")

    else:
        bookings.append(book)  # record the booking
        seat_numbers.discard(book)  # remove booked seat
        print(f"You have successfully booked seat number {book}. Kindly have your seat.")
        print(f"Here are the available seats left:\n{seat_numbers}")

except ValueError:
    print("Invalid input! Please enter a valid seat number (1 - 50).")