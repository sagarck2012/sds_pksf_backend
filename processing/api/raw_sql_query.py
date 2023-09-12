def get_harvest_for_packaging(start_date, end_date, crop_type_id):
    query = f'''SELECT 
  production_harvesting.id,
  production_harvesting.harvest_cycle,
  production_harvesting.quantity,
  production_harvesting.status,
  production_harvesting.created_at,
  production_harvesting.plot_id,
  production_plot.crop_id,
  farm_crop.name,
  production_plot.crop_type_id,
  farm_croptype.eng_name,
  farm_croptype.local_name,
  production_plot.crop_variant 
FROM
  production_harvesting 
  LEFT JOIN production_plot 
    ON production_plot.id = production_harvesting.plot_id 
  LEFT JOIN farm_crop 
    ON farm_crop.id = production_plot.crop_id 
  LEFT JOIN farm_croptype 
    ON farm_croptype.id = production_plot.crop_type_id 
WHERE production_harvesting.status IN (
    'partially harvested',
    'fully harvested'
  ) 
  AND production_plot.crop_type_id = {crop_type_id} 
  AND production_harvesting.created_at BETWEEN '{start_date}' 
  AND '{end_date}' 
GROUP BY production_harvesting.harvest_cycle'''

    return query


# def get_created_packaging_list(start_date, end_date, crop_type_id):
def get_created_packaging_list(crop_type_id):
    query = f'''SELECT 
  * 
FROM
  process_packaging_master 
   
  LEFT JOIN farm_crop 
    ON farm_crop.id = process_packaging_master.`crop_id` 
  LEFT JOIN farm_croptype 
    ON farm_croptype.id = process_packaging_master.`crop_type_id` 

  WHERE process_packaging_master.crop_type_id = {crop_type_id} '''

  # AND process_packaging_master.created_at BETWEEN '{start_date}'
  # AND '{end_date}'

    return query


def get_sticker_of_package(processing_id):
    query = f'''SELECT * FROM process_packaging_detail WHERE processing_id LIKE '{processing_id}' '''
    return query

