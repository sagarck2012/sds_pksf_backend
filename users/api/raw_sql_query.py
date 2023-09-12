def role_privilege(role_id):
    query = f'''SELECT 
  i_privilege.id,
  i_privilege.role_id,
  i_privilege.menuname_id,
  i_menu_name.name menu_name,
  i_privilege.modulename_id,
  i_module_name.modulename module_name,
  i_privilege.url_id,
  i_module_action.url,
  i_privilege.is_allowed 
FROM
  i_privilege 
  LEFT JOIN i_menu_name 
    ON i_menu_name.id = i_privilege.menuname_id 
  LEFT JOIN i_module_name 
    ON i_module_name.id = i_privilege.modulename_id
  LEFT JOIN i_module_action 
    ON  i_module_action.id = i_privilege.url_id
WHERE i_privilege.role_id = {role_id}
ORDER BY menuname_id'''
    return query

