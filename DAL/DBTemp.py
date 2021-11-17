from DAL.DBUtil import DBUtil
from Entities import Temperature


class DBTemp:
    dta = DBUtil()

    def select_all_temperatures(self):
        return self.dta.execute_select_query("temp")

    def select_temperature(self, id: int):
        return self.dta.execute_select_query("temp", " WHERE id = "+str(id))

    def insert_temperature(self, temperature: Temperature):
        print(temperature.datetime)
        print(temperature.temp)
        print(temperature.humidity)
        return self.dta.execute_insert_query(temperature)