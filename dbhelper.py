import mysql.connector

class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='******',
            database = 'indigo' # optional
            )

            self.mycursor = self.conn.cursor()
            print('Connection established')
        except:
            print('Connection error')

    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""SELECT DISTINCT(Destination) FROM indigo.flights_data
        UNION
        SELECT DISTINCT(Source) FROM indigo.flights_data""")

        data = self.mycursor.fetchall()
        
        for item in data:
            city.append(item[0])

        return city
    
    def fetch_all_flights(self, source, destination):

        self.mycursor.execute("""SELECT Airline,Route, Dep_Time, Duration, Price FROM indigo.flights_data
        WHERE Source = '{}' AND Destination = '{}'""".format(source, destination))

        data = self.mycursor.fetchall()

        return data
    
    def fetch_airline_frequency(self):
        
        airline = []
        frequency = []

        self.mycursor.execute("""
        SELECT Airline, COUNT(*) FROM indigo.flights_data
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
            
        return airline, frequency

    def busy_airport(self):

        city = []
        frequency = []

        self.mycursor.execute("""SELECT Source, COUNT(*) FROM (SELECT Source FROM indigo.flights_data
				UNION ALL
				SELECT Destination FROM indigo.flights_data) t
                GROUP BY t.Source   
                ORDER BY COUNT(*) DESC 
            """)
        
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])
            
        return city, frequency
    
    def daily_frequency(self):

        date = []
        frequency = []

        self.mycursor.execute("""SELECT Date_of_Journey, COUNT(*) FROM indigo.flights_data
            GROUP BY Date_of_Journey
            """)
        
        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])
            
        return date, frequency
