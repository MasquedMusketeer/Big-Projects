import day_month_module as damom
import data_stripper_module as dastrm
import transport_calc_module as tracalm

print(damom.dayMonthEncoder(5,12))
print(dastrm.dateStripper(damom.dayMonthEncoder(5,12)))
print(tracalm.totalValueCalculator(dastrm.dateStripper(damom.dayMonthEncoder(5,12))))
