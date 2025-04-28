import random
import datetime

def simulate_parcel_tracking():
    parcel_ids = ['PKG001', 'PKG002', 'PKG003']
    locations = ['Warehouse', 'Airport', 'Local Facility', 'Out for Delivery']
    parcel = random.choice(parcel_ids)
    location = random.choice(locations)
    timestamp = datetime.datetime.now().isoformat()
    
    print(f"[{timestamp}] Parcel {parcel} is at {location}.")

def simulate_reminder():
    reminders = [
        "Your parcel is on the way!",
        "Your parcel will arrive today.",
        "Please be available to receive your parcel.",
        "Your parcel has been delivered!"
    ]
    print(random.choice(reminders))

if __name__ == "__main__":
    simulate_parcel_tracking()
    simulate_reminder()
