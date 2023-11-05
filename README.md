# realtimepolling
# Real-Time Polling App with Django

Welcome to the Real-Time Polling App with Django! This application allows users to create and participate in polls, with real-time updates of poll results using AJAX.

![App Screenshot](/screenshot/homepage.png)

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Create and manage polls with questions and choices.
- Users can vote for their preferred choice in each poll.
- Real-time voting and updates using WebSockets.
- Clean and responsive user interface.

## Prerequisites

- Python 3.11.4
- Django 4.2.6
- Basic understanding of Django, web development

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hraju115/realtimepolling.git
   cd realtimepolling
   ```

2. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

4. Load sample data (optional):
   ```bash
   python manage.py loaddata polling/fixtures/sample_data.json
   ```

## Usage

1. Run the development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application in your web browser:
   Open http://localhost:8000/ in your browser to start using the app.

3. Create polls, vote, and view real-time poll results.