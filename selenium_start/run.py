from back import Booking


with Booking() as bot:
    bot.open_page()
    bot.check_page()
    bot.popup_close()
    bot.select_city(place_from="Accra")
    bot.select_destination(place_to="Berlin")
    bot.select_dep_date(day="Friday", month="Oct", date="24", year=2025)
    bot.intentional_wait(30)