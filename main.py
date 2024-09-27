#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
from notification_manager import NotificationManager

my_spreadsheet = DataManager()
sheet_data = my_spreadsheet.sheet_data
print(sheet_data)
flight_search = FlightSearch()
#   for sheet in sheet_data:
#       flight_search.update_data(sheet)
#       payload = {"price" : sheet}
#       my_spreadsheet.put_data(payload)

notification_manager = NotificationManager()


tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime("%Y-%m-%d")
flight_check = FlightData()

for data in sheet_data:
    flight_data = flight_search.check_flights(data, departure_date=tomorrow, return_date=six_month_from_today)
    print(flight_data)
    cheapest_flight = flight_check.find_cheapest_flight(flight_data)
    if cheapest_flight.price != 'N/A':
        cheapest_price = float(cheapest_flight.price)
        if  cheapest_price < data['lowestPrice']:
            notification_manager.send_msg(
                flight_price=cheapest_flight.price,
                from_iata=cheapest_flight.origin_airport,
                to_iata=cheapest_flight.destination_airport,
                from_date=cheapest_flight.out_date,
                to_date=cheapest_flight.return_date)






