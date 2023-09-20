import day_month_module as damom
import data_stripper_module as dastrm
import transport_calc_module as tracalm
import read_write_module as rwm

mainMatrix = rwm.read_Write_module('r',0)
mainMatrix.pop(0)
last_report = dastrm.dataStripper(mainMatrix.pop(-1))
transport_report = tracalm.totalValueCalculator(damom.dayMonthEncoder(dastrm.dateStriper(last_report.pop(0))))
print(transport_report)
