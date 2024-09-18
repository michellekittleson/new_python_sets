# Task 1: Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to (.intersection())
def find_intersection(airline1, airline2):
    intersection = airline1.intersection(airline2)
    print(f"Destination(s) that both airlines fly to: {intersection}")
find_intersection(our_routes, competitor_routes)

# 2. Destinations unique to your airline (.difference())
def find_unique(airline1, airline2):
    unique = airline1.difference(airline2)
    print(f"Destination(s) unique to our airline: {unique}")
find_unique(our_routes, competitor_routes)

# 3. Whether there are any destinations that neither airline shares (.symmetric_difference())
def neither_shares(airline1, airline2):
    neither = airline1.symmetric_difference(airline2)
    print(f"Destination(s) that neither airline shares: {neither}")
neither_shares(our_routes, competitor_routes)