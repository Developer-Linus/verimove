# VeriMove: Vehicle Verification and Movement Tracking System

## Project Overview

VeriMove is a robust system designed to track vehicle movements in and out of a facility, automatically verifying attendance for staff and generating allowance reports. It provides a secure and efficient way to manage vehicle logs, associate them with staff members, and ensure accurate record-keeping for financial and audit purposes.

## How It Works

1.  **Vehicle & Staff Registration**: System administrators can register staff members and their associated vehicles.
2.  **Automated Vehicle Logging**: As vehicles enter or exit, the system captures the license plate, timestamp, and an image of the vehicle.
3.  **Staff & Vehicle Identification**: The system identifies the vehicle and links it to the registered staff member.
4.  **Attendance Verification**: The first daily entry of a staff member's vehicle is used to mark their attendance for the day.
5.  **Allowance Reporting**: At the end of the month, the system calculates allowances for eligible staff based on their attendance and generates a report.

## Features

*   **Staff & Vehicle Management**: Easily add, edit, and manage staff and vehicle information.
*   **Real-time Vehicle Logging**: See a live feed of vehicles entering and exiting the premises.
*   **Automated Attendance**: Attendance is automatically marked based on vehicle entry.
*   **Allowance Generation**: Generate monthly allowance reports with a single click.
*   **Secure Access**: Role-based access control to ensure data privacy and security.
*   **Audit Trail**: Maintain a complete history of vehicle movements for auditing purposes.

## Technology Stack

*   **Backend**: Django, Django REST Framework
*   **Database**: PostgreSQL
*   **Frontend**: HTML, CSS, JavaScript
*   **Package Management**: uv

## How to Run The App Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Developer-Linus/verimove.git
    cd verimove
    ```

2.  **Create a virtual environment and install dependencies:**
    - Make sure you have `uv` installed (`pip install uv`).
    - Create and activate the virtual environment:
    ```bash
    uv venv
    source .venv/bin/activate
    ```
    - Install the dependencies:
    ```bash
    uv sync 
    ```

3.  **Set up the database:**
    - Make sure you have PostgreSQL running.
    - Create a `.env` file in the project root and add your database credentials:
    ```
    DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
    SECRET_KEY=your-secret-key
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
The application will be available at `http://127.0.0.1:8000`.

## Security

*   **Authentication & Authorization**: Access to the system is restricted to authenticated users. The system uses Django's built-in authentication and authorization, with different roles (e.g., Admin, Security Staff) having different levels of access.
*   **Data Protection**: Sensitive data is protected, and all vehicle logs are tamper-proof.
*   **CSRF Protection**: The application is protected against Cross-Site Request Forgery attacks.

## Database Design
![Database Design](database_design.png)

## Screenshots
![Hero Image](hero.png)
_The main landing page for the VeriMove system._

![Vehicle Logging Pipeline](pipeline.png)
_The pipeline for processing vehicle images and logging entries._

![Admin Dashboard](dashboard.png)
_The admin dashboard for managing the system._

![Generate Allowances](generate_allowances.png)
_Generating monthly allowance reports for staff._

