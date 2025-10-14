from back import Booking


with Booking() as bot:
    bot.open_page()
    # bot.check_page()
    bot.try_code()