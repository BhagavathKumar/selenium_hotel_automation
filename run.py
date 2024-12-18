from booking.booking import Booking
import time

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.allow_cookies()
        time.sleep(2)
        bot.close_sign_in_popup()
        bot.change_currency(currency=input(
            "Enter Currency (ex. USD, EUR, AUD): "
        ))
        bot.close_sign_in_popup()
        bot.destination_to_go(
            place_to_go=input("Enter the Destination: "))
        bot.date_selection(
            check_in_date=input(
                "Enter Check-In Date: ex format 'Sat Jan 18 2025': "
                ), 
            check_out_date=input(
                "Enter Check-Out Date: ex format 'Mon Jan 20 2025': "
                ))
        bot.guest_selection(
            no_of_rooms=input(
                "Enter Number of Rooms (01 - 20): "
                ), 
            no_of_adults=input(
                "Enter Number of Adults (01 - 40): "
                ))
        bot.click_submit_button()
        bot.apply_filteration()
        bot.report_hotel_table()
        
except Exception as e:
    if "in PATH" in str(e):
        print(
            "You are To run the bot from command line \n"
            "please add path to your selenium drivers \n"
            "windows: \n"
            "set PATH=%PATH;C:path-to-your-folder \n \n"
            "Linux: \n"
            "PATH=%PATH:/path/toyour/folder/ \n"
        )
    else:
        raise