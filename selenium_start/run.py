from back import Booking


with Booking() as bot:
    bot.open_page()
    bot.check_page()
    bot.popup_close()
    bot.select_city(place_from="Accra")
    bot.intentional_wait(30)