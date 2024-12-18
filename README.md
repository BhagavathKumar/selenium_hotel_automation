# Selenium Booking Search Automation

## Overview
This project automates the process of searching for hotel rooms in MakeMyTrip website using Selenium WebDriver. It allows users to input travel details, apply filters, and retrieve a list of the top hotels or rooms within their budget, sorted by price and other criteria. The results are displayed in a clean, tabular format on the console. The results will include `Hotel Name`, `Hotel Location`, `Hotel Rating` and `Hotel Price`.

## Features
- User-friendly: Intuitive prompts guide you through the input process, ensuring a seamless user experience.
- Customizable: Easily modify search criteria such as location, currency, check-in/out dates, number of rooms, and guests.
- Filtered Results: Apply advanced filters like budget range, price sorting (Low to High), and ratings (4.2+).
- Detailed Reports: Retrieve comprehensive hotel details, including names, locations, ratings, and prices, displayed in a clear tabular format.
- Error Handling: Incorporates troubleshooting for common Selenium issues, such as WebDriver setup errors or missing dependencies.
- Scalable Design: The modular structure allows for adding more filters, functionalities, or different search platforms in the future.

## Output:
Detailed and filtered hotel reports printed on the console
Reliable and customizable functionality

## Directory Structure
```
bot/
├── booking/
│   ├── booking.py               # Core booking automation logic
│   ├── booking_filteration.py   # Handles filtering logic
│   ├── booking_report.py        # Generates and displays reports
│   ├── constants.py             # Stores reusable constants
└── run.py                       # Entry point for the application
```

## Getting Started
### Prerequisites
- Python 3.8+
- Selenium WebDriver
- Google Chrome and ChromeDriver

### Installation
1. Clone the repository:
```
git clone https://github.com/your-repo/selenium-hotel-automation.git
cd selenium-hotel-automation
```
2. Install required Python packages:
```
pip install -r requirements.txt
```
3. Download and set up [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads) compatible with your Chrome version.

## Usage
1. Navigate to the project directory.
2. Run the script:
```
python run.py
```
3. Follow the prompts to enter:
```
Enter Currency (ex. USD, EUR, AUD):
Enter the Destination:
Enter Check-In Date: ex format 'Sat Jan 18 2025':
Enter Check-Out Date: ex format 'Mon Jan 20 2025':
Enter Number of Rooms (01 - 20):
Enter Number of Adults (01 - 40):
Enter Minimum Budget Value:
Enter Maximum Budget Value:
```
4. View the filtered and sorted hotel list in the console.
Example output:
```
+---------------------------------------------------------+---------------------------+----------------+----------------+
| Hotel Name                                              | Hotel Location            |   Hotel Rating | Hotel Prices   |
+=========================================================+===========================+================+================+
| St Christopher's Inn, Hammersmith - Hostel              | Hammersmith               |            3.5 | € 27
|
+---------------------------------------------------------+---------------------------+----------------+----------------+
| Kensal Green Backpackers 1                              | White City                |            3.5 | € 29
|
+---------------------------------------------------------+---------------------------+----------------+----------------+
| Safestay London Kensington Holland Park                 | Central London            |            3.5 | € 29
|
+---------------------------------------------------------+---------------------------+----------------+----------------+
```
## Customization
- Modify filters in `booking.py` to add or change criteria.
Adjust reporting details in `booking_report.py`.

## Reference
This project is inspired by a course provided by [JimShapedCoding](https://www.youtube.com/channel/UCU8d7rcShA7MGuDyYH1aWGg). Special thanks to Jim for providing detailed guidance on Selenium-based automation.

## License
This project is licensed under the MIT License. See [Licence](LICENCE.txt) file for details.
