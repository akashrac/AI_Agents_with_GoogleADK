from datetime import datetime, timedelta

def calculate_trip_budget(listings: list, nights: int) -> dict:
    """Calculate total trip budget from listings"""
    total_cost = sum([listing['price'] * nights for listing in listings])
    avg_per_night = total_cost / len(listings) if listings else 0
    
    return {
        "status": "success",
        "total_cost": total_cost,
        "average_per_night": avg_per_night,
        "num_properties": len(listings),
        "breakdown": [
            {
                "property": listing['name'],
                "nights": nights,
                "total": listing['price'] * nights
            }
            for listing in listings
        ]
    }

def format_search_dates(start_date: str, num_nights: int) -> dict:
    """Format dates for Airbnb search"""
    checkin = datetime.strptime(start_date, "%Y-%m-%d")
    checkout = checkin + timedelta(days=num_nights)
    
    return {
        "checkin": checkin.strftime("%Y-%m-%d"),
        "checkout": checkout.strftime("%Y-%m-%d")
    }
