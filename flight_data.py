from datetime import datetime


def date_fix(date):
    datetime_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    fixed_date = datetime_obj.strftime('%Y-%m-%d')
    return fixed_date



class FlightData:
    def __init__(self, price='', origin_airport='', destination_airport='', out_date='', return_date=''):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def find_cheapest_flight(self, data_dict):

        if data_dict is None or not data_dict['data']:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

        data = data_dict['data'][0]
        price = data['price']['total']
        origin_airport = data['itineraries'][0]['segments'][0]['departure']['iataCode']
        destination_airport = data['itineraries'][0]['segments'][0]['arrival']['iataCode']
        out_date = date_fix(data['itineraries'][0]['segments'][0]['departure']['at'])
        return_date = date_fix(data['itineraries'][1]['segments'][0]['arrival']['at'])

        cheapest_flight = FlightData(price, origin_airport, destination_airport, out_date, return_date)

        cheapest_price = cheapest_flight.price

        for data in data_dict['data']:
            flight_price = data['price']['total']
            if cheapest_price > flight_price:
                price = data['price']['total']
                origin_airport = data['itineraries'][0]['segments'][0]['departure']['iataCode']
                destination_airport = data['itineraries'][0]['segments'][0]['arrival']['iataCode']
                out_date = date_fix(data['itineraries'][0]['segments'][0]['departure']['at'])
                return_date = date_fix(data['itineraries'][1]['segments'][0]['arrival']['at'])

            cheapest_flight = FlightData(price, origin_airport, destination_airport, out_date, return_date)


        return cheapest_flight


