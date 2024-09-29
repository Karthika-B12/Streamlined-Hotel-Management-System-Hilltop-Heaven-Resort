
# Streamlined-Hotel-Management-System-Hilltop-Heaven-Resort

## Overview

The **Hotel Management System** is designed to manage hotel operations for **Hilltop Heaven Resort**. This application provides features for both **guests** and **administrative users**. It allows guests to book rooms, order food, avail room services, and access other resort amenities, while administrative users can manage guest data, room availability, bookings, and service details.

## Features

### Guest Portal:
- **Signup & Profile Management**: Guests can create accounts and update their profile details.
- **Room Booking**: Guests can book rooms from various branches of the resort.
- **Booking History**: View previous and ongoing bookings.
- **Restaurant & Room Service**: Order food and beverages directly from the resort's restaurant.
- **Resort Amenities**: Access services like spa, indoor/outdoor games, and more.

### Admin Portal:
- **Account Management**: Administrators can manage their profiles and create new administrative accounts.
- **Room Management**: Add and update room details, including availability and types.
- **Service Management**: Manage restaurant, room services, and resort amenities.
- **User & Booking Management**: View and manage guest profiles, bookings, and services availed.

## Database Schema

The system uses the following database tables:
- **Branch**: Stores information about resort branches.
- **Room_Type**: Details about various room types offered by the resort.
- **Rooms**: Specific rooms available at different branches.
- **Services**: Lists available services like restaurant items, room services, and amenities.
- **User_Admin**: Stores user and admin profiles.
- **Booking_Details**: Records all booking information made by the guests.
- **User_Services**: Tracks the services availed by the guests during their stay.

## Installation Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Karthika-B12/Streamlined-Hotel-Management-System-Hilltop-Heaven-Resort.git
   cd hotel-management-system
   ```

2. **Install dependencies**:
   Ensure you have `Python`, `Tkinter`, `MySQL`, and other required libraries installed. Use `pip` to install any missing dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   - Create a MySQL database named `hotel`.
   - Import the database schema by running the SQL scripts provided in the `/database` folder.

4. **Run the Application**:
   ```bash
   python project full code .py
   ```

## Usage

1. **For Guests**:
   - Signup for a new account and log in.
   - Browse room availability, book rooms, and access restaurant and room services.

2. **For Admin**:
   - Log in with admin credentials.
   - Manage room types, bookings, and guest profiles.

## Output

You can view the output of the system here:
![Screenshot 2024-09-29 130542](https://github.com/user-attachments/assets/6412b000-8fec-4b11-b6cd-96f8566b1c19)


## Resources

- **MySQL**: Database management system used for storing data.
- **Tkinter**: Python library used for building the GUI.
- **MySQL Connector**: Used to connect the Python application with the MySQL database.

## Contact

For any queries or further information, please contact Karthika at karthikapanchu2004@gmail.com.

---
