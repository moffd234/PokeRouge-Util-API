import logging

from flask import Blueprint, jsonify, Response
from Application.Models.Pokemon import Pokemon

team_checker_bp: Blueprint = Blueprint('team_checker_bp', __name__)
team_checker_logger: logging.Logger = logging.getLogger("api")

