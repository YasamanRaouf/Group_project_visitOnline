# Visit Online - Online Doctor Appointment Booking System
This is a group project for the course **Django Web Development** at **Quera Bootcamp**. The project aims to create an online doctor appointment booking system using Django.

doctor-app-ali: view functionality (view) for displaying a Doctor's details and availablity has been created

doctor-app-ali: doctor-ali-view-detail-availability branch has been created , we started to design the view in which we show details and available timeslots to visit for doctors.


- [Visit Online - Online Doctor Appointment Booking System](#visit-online---online-doctor-appointment-booking-system)
  - [Overview](#overview)
  - [Key Features:](#key-features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Architecture](#architecture)
  - [Contributors](#contributors)

## Overview

This project is designed to create a **user-friendly online appointment booking system for doctors**. Patients can seamlessly book appointments, and doctors can manage their availability and schedules with ease. The system is developed using Django and aims to streamline the interaction between healthcare providers and patients.

## Key Features:

1. **Comprehensive Doctor Management**  
   Admins can effortlessly add and organize doctors by their specialties, manage their availability, and set consultation fees with ease.

2. **Smart Doctor Search**  
   Patients can quickly find doctors by searching through names or specialties, ensuring they connect with the right professional.

3. **Seamless Appointment Booking**  
   Patients can choose from available time slots, make secure payments, and receive instant email confirmations for their appointments.

4. **Patient Feedback and Ratings**  
   After their appointments, patients can share their experiences by rating doctors and leaving valuable feedback.

5. **Enhanced Security and Access**  
   Enjoy secure login through OTP verification, with an optional OAuth2 integration for logging in via Google.

6. **Production-Ready Design**  
   The system is fully prepared for deployment, featuring optimized server configurations and efficient file management for smooth operation.

## Requirements

- Python 3.x
- Django 3.x or higher
- PostgreSQL or any other supported database

## Installation

1. Clone the repository:

   ```bash
   git clone https://gitlab.com/delta7-g3/visitonline.git
    ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Django migrations:

   ```bash
    python manage.py migrate
    ```

4. Create a superuser account:
  
   ```bash
   python manage.py createsuperuser
   ```

5. Start the Django development server:

   ```bash
    python manage.py runserver
    ```

## Architecture

The system leverages Django’s Model-View-Template (MVT) architecture, ensuring a clean and scalable structure. It is also built to be production-ready with appropriate server configurations and security measures.

## Contributors

- [seyed mohammadali hashemi](https://gitlab.com/sma.golestani) - Project Manager
- [Mahan MI](https://gitlab.com/mahanmi) - Lead Developer
- [Ali Farokhnia](https://gitlab.com/farokhniaali900) - Developer
- [Amin Mohammad Davoudi](https://gitlab.com/AMD921) - Developer
- [Fateme Nateghi](https://gitlab.com/ftm.ntghi) - Developer
- [Yasaman Raoufmoghadam](https://gitlab.com/YasamanRaouf) - Developer
- [Siamak Kamanabroo](https://gitlab.com/Siamakka) - Developer
  

