# Rocket Launch Management and Booking System

A console-based Python application for managing rocket launches and customer bookings, with separate **admin** and **user** roles, built on a flat-file (`.txt`) storage backend.

## Features

**Admin**
- Manage rocket specifications (height, width, mass, payload capacity to LEO/GTO/SSO) and pricing
- Schedule and manage launch slots with date validation (leap-year aware)

**User**
- Sign up / log in
- Browse available rockets and launch slots, and book a launch
- View active bookings and booking history
- Per-user remarks/notes tracking

## Project Structure

```
├── main.py                        # Entry point — login menu (admin / user)
├── package/
│   ├── login.py                   # Admin & user authentication
│   ├── user.py                    # User signup, login, menu, bookings
│   ├── rocket.py                  # Rocket specs & pricing (read/write helpers)
│   └── planningAndScheduling.py   # Launch slot scheduling, date validation
├── spec.txt                       # Rocket specifications database
├── price.txt                      # Rocket pricing database
├── launch_slot.txt                # Scheduled launch slots
├── user.txt                       # Registered users
├── booking_history.txt            # Global booking history
└── <username>_*.txt               # Per-user active bookings, history, remarks
```

Data is persisted as pipe/colon-delimited records in plain `.txt` files — no external database required.

## Running

```bash
git clone https://github.com/devSaksham/Rocket-Launch-Management-and-Booking-System.git
cd Rocket-Launch-Management-and-Booking-System
python main.py
```

You'll be prompted to log in as **Admin** or **User** (with sign-up available for new users), then guided through the relevant menu.

## Requirements

- Python 3, standard library only — no external dependencies.
