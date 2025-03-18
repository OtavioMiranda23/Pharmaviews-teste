import uuid
from src.entities.Action import Action
class ActionRepository:
    def __init__(self, db_connection_func):
        self.db_connection_func = db_connection_func

    def save(self, action: Action):
        connection = self.db_connection_func()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO action(id, action_type, expect_date, investment)
            VALUES (%s, %s, %s, %s)
        """, (str(action.id), action.id_action_type, action.date, action.investment))
        connection.commit()
        cursor.close()
        connection.close()

    def get_all_actions(self):
        connection = self.db_connection_func()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT action.id, action_types.name, action.action_type, action.expect_date, action.investment
            FROM action
            INNER JOIN action_types ON action.action_type = action_types.id;
        """)
        actions = cursor.fetchall()
        actions_entity = list(
            map(lambda action: Action(action[0], action[2], action[1], action[3], action[4]), actions))
        cursor.close()
        connection.close()
        return actions_entity

    def get_action_by_id(self, action_id: uuid.UUID):
        connection = self.db_connection_func()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT action.id, action_types.name, action.action_type, action.expect_date, action.investment
            FROM action
            INNER JOIN action_types ON action.action_type = action_types.id
            WHERE action.id = %s;
        """, [action_id])
        action = cursor.fetchone()
        action_entity = Action(action[0], action[2], action[1], action[3], action[4])
        cursor.close()
        connection.close()
        return action_entity
    
    def get_action_name_by_id(self, action_id: str):
        connection = self.db_connection_func()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM action_types WHERE id = %s", (action_id,))
        action = cursor.fetchone()
        cursor.close()
        connection.close()
        return action[1]
    
    def get_all_types_actions(self):
        connection = self.db_connection_func()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM action_types;
        """)
        types = cursor.fetchall()
        cursor.close()
        connection.close()
        return types
    
    def delete_action_by_id(self, action_id: str):
        connection = self.db_connection_func()
        cursor = connection.cursor()
        
        try:
            cursor.execute("DELETE FROM action WHERE action.id = %s", (action_id,))
            connection.commit()
        finally:
            cursor.close()
            connection.close()

    def update_action(self, action_id: str, action: Action):
        connection = self.db_connection_func()
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                UPDATE action
                SET action_type = %s, expect_date = %s, investment = %s
                WHERE id = %s
            """, (action.id_action_type, action.date, action.investment, action_id))

            connection.commit()
        finally:
            cursor.close()
            connection.close()
