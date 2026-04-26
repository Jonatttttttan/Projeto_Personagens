from flask import render_template, request, redirect, flash, url_for, Blueprint
import os

import pandas as pd
import numpy as np
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

principal_bp = Blueprint("principal", __name__)

@principal_bp.route("/")
def home():
    return render_template("home.html")


