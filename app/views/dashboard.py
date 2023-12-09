# dashboard.py
from flask import Blueprint, render_template, request, session, redirect, url_for
import logging

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# Set up a simple logger
'''logging.basicConfig(filename='activity.log', level=logging.INFO)'''


@dashboard_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session.get('username'):
        return redirect(url_for('login'))

    return render_template('dashboard/dashboard.html')