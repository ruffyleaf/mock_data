from AirportIncidentGenerator import Incident
import datetime
import random

def random_date_between(startdate_y, startdate_m, startdate_d, enddate_y, enddate_m, enddate_d):
    startdate = datetime.date(startdate_y, startdate_m, startdate_d)
    enddate = datetime.date(enddate_y, enddate_m, enddate_d)

    time_between_dates = enddate - startdate
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = startdate + datetime.timedelta(days=random_number_of_days)

    return random_date

def main():
    incident_categories = ['oil_spill', 'bird_strike', 'tow_truck']
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'july']
    filename = 'testoutput.csv'

    for month in months:
        if month == 'jan':
            for _ in range(0,32):
                lam = 30
                date = random_date_between(2021, 1, 1, 2021, 1, 31)
                incident = Incident(incident_categories, date, lam)
                incident.write_data(filename)

if __name__ == "__main__":
    
    main()