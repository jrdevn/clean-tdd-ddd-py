from .exceptions import CheckinDateCannotBeAfterCheckoutDate, CustomerCannotBeBlank
from datetime import datetime
from booking_service.domain.customers.entities import Customer
from booking_service.domain.rooms.entities import Room

class Booking(object):
    checkin: datetime
    checkout: datetime
    customer: Customer
    margin: float
    room: Room

    def __init__(self, checkin: datetime, checkout: datetime, customer: Customer):
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer

    def close_booking(self):
        self.is_valid()

    def is_valid(self):
        if self.checkin > self.checkout:
            raise CheckinDateCannotBeAfterCheckoutDate("Checkin cannot be after Checkout")
        elif not self.customer:
            raise CustomerCannotBeBlank("Customer is a required information")

        return True