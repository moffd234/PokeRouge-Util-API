from flask import Blueprint
from Application.Utils.TypeUtils import TypeUtils

weaknesses_bp: Blueprint = Blueprint("weaknesses_bp", __name__)
type_util: TypeUtils = TypeUtils()
