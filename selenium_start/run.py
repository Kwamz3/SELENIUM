from back import Booking


with Booking() as bot:
    bot.open_page()
    bot.check_page()
    bot.popup_close()
    bot.select_city(place_from="Accra")
    bot.select_destination(place_to="Berlin")
    bot.select_dep_date(day="Friday", month="October", date="31", year=2025)
    bot.select_ret_date(day="Monday", month="December", date="28", year=2025)
    bot.select_passengers(adl_cnt=2, chd_cnt=3, inf_cnt=2)
    bot.intentional_wait(30)