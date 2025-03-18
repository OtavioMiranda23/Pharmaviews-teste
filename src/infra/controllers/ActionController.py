from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
from src.application.usecase.GetActionById import GetActionById
from src.application.usecase.GetActions import GetActions
from src.application.usecase.CreateAction import CreateAction
from src.application.usecase.DeleteAction import DeleteAction
from src.application.usecase.UpdateAction import UpdateAction
from src.application.usecase.GetTypesActions import GetTypesActions

import decimal
from datetime import datetime


class ActionController:
    def __init__(self, repository):
        self.blueprint = Blueprint('action', __name__)
        self.repository = repository
        self._register_routes()

    def _register_routes(self):
        self.blueprint.route('/action', methods=['POST'])(self.create_action)
        self.blueprint.route('/actions', methods=['GET'])(self.get_actions)
        self.blueprint.route('/action/<action_id>', methods=['GET'])(self.get_action_by_id)
        self.blueprint.route('/action', methods=['PUT'])(self.update_action)
        self.blueprint.route('/action', methods=['DELETE'])(self.delete_action_by_id)
        self.blueprint.route('/types', methods=['GET'])(self.get_type_actions)

    def create_action(self):
        data = request.get_json()
        dateRaw = data.get('date')
        action_datetime = datetime.strptime(dateRaw, "%Y-%m-%d")
        investmentRaw = data.get('investment')
        investment = decimal.Decimal(investmentRaw)
        action_type = int(data.get('action_type'))
        action_entity = CreateAction(self.repository).execute(action_type, action_datetime, investment)
        return jsonify({
            "data": { 
                "id": action_entity.id, 
                "name": action_entity.action_name 
                }
            }), 200
    
    def get_actions(self):
        actions = GetActions(self.repository).execute();
        return jsonify({"data": [action.to_dict() for action in actions]}),200
    
    def get_action_by_id(self, action_id):
        action_entity = GetActionById(self.repository).execute(action_id)
        return jsonify({"data": {
                            "id": action_entity.id,
                            "name": action_entity.action_name,
                            "date": action_entity.date,
                            "investment": action_entity.investment
                        }
                    }), 200
    def delete_action_by_id(self):
        data = request.get_json()
        id = data.get('id')
        DeleteAction(self.repository).execute(id)
        return jsonify({}), 200
    
    def update_action(self):
        try:
            action_data = request.get_json()
            print(action_data)
            action_id = action_data.get("action_id")
            updated_action = UpdateAction(self.repository).execute(action_id, action_data)
            print(updated_action)
            return jsonify({
                "id": str(updated_action.id),
                "action_type": updated_action.id_action_type,
                "action_name": updated_action.action_name,
                "expect_date": updated_action.date,
                "investment": updated_action.investment
            }), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 404

        except Exception as e:
            return jsonify({"error": "Erro interno no servidor"}), 500
        
    def get_type_actions(self):
        types = GetTypesActions(self.repository).execute();
        return jsonify({"data": types}), 200