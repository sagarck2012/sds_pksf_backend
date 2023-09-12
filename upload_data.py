import pymysql
import pandas

db = pymysql.connect("localhost", "root", "Admin@2019", "pksfdb")
cursor = db.cursor()


def insert_into_db_table(table_name, data_dict):
    print(f"data inside insert method:{data_dict}")

    # update sql statement based on your table column and data_dict
    sql = f"INSERT INTO {table_name} (name,crop_id, local_name,scientific_name,major_nutrient) " \
          f"VALUES ('{data_dict['name']}', {data_dict['crop_id']}, '{data_dict['local_name']}'," \
          f"'{data_dict['scientific_name']}','{data_dict['major_nutrient']}')"

    # sql = f"INSERT INTO {table_name} (name,soil_type, harvesting_period,expected_production,seasonal,vegetable_type_id ) " \
    #       f"VALUES ('{data_dict['name']}', '{data_dict['soil_type']}', '{data_dict['harvesting_period']}'," \
    #       f"'{data_dict['expected_production']}','{data_dict['seasonal']}', '{data_dict['vegetable_type_id']}')"
    print(f"Sql query: {sql}")
    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        cursor.execute(sql)
        db.commit()
    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
        db.rollback()

    # cursor.close()
    # db.close()


def doc_read_farm_croptype(doc_path, excel_col_names):
    df = pandas.read_excel(doc_path)
    try:
        df_selected = df[excel_col_names]
        for index, row in df_selected.iterrows():
            print(row)
            data_dict = {}
            for col in excel_col_names:
                data_dict[col] = row[col]
            # replace "farm_croptype" with your db table
            insert_into_db_table("farm_croptype", data_dict)
        # cursor.close()
        # db.close()

    except Exception as e:
        print(e)


file_path = "E:\PKSF\Crop Data\crop-name-updated.xlsx"
# file_path = "E:\PKSF\Crop Data\crop-variant.xlsx"
excel_col_name = ['name', 'crop_id', 'local_name', 'scientific_name', 'major_nutrient']
# excel_col_name = ['name', 'soil_type', 'harvesting_period', 'expected_production', 'seasonal', 'vegetable_type_id']
doc_read_farm_croptype(file_path, excel_col_name)
# doc_read_farm_vegetable("E:\PKSF\Crop Data\crop-variant.xlsx")