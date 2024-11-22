# from flask import request, session, redirect, render_template, make_response
# from base import app
# from base.com.vo.login_vo import loginVO
#
#
# # user_name = "admin@gmail.com"
# # password = "admin12345"
#
# # Define the logout route
# @app.route('/logout', methods=['POST'])
# def logout():
#     # Remove the user's session data
#     session.clear()
#     session["logged_in"] = False
#     # session["logged_in_user"] = None
#     # Redirect the user to the login page
#     response = make_response(redirect("/"))
#     # Add cache control headers to prevent caching
#     response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '0'
#     return response
#
#
# # Add cache control headers to prevent caching for all routes
# @app.after_request
# def add_cache_control(response):
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Pragma"] = "no-cache"
#     response.headers["Expires"] = "0"
#     return response
#
#
# # Login route
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if session.get('logged_in'):
#         return redirect('/admin/load_dashboard')
#
#     if request.method == 'POST':
#         un = request.form.get("userName")
#         pwd = request.form.get("pw")
#
#         # Query the database to check user credentials
#         user = loginVO.query.filter_by(user_name=un, password=pwd).first()
#
#         if user:
#             session['logged_in'] = True
#             app.logger.info(f"User {un} logged in successfully.")
#             return redirect('/admin/load_dashboard')
#         else:
#             app.logger.error("Login failed. Invalid username or password.")
#             return render_template('admin/login.html',
#                                    error='Invalid username or password')
#
#     return render_template('admin/login.html')
#
#
# # Dashboard route
# @app.route('/admin/load_dashboard')
# def admin_load_dashboard():
#     if session.get('logged_in'):
#         return render_template('admin/index.html')
#     else:
#         return redirect('/')
#
#
# # Index route
# @app.route('/')
# def hello_world():
#     if session.get('logged_in'):
#         return redirect('/admin/load_dashboard')  # Redirect authenticated users to the dashboard
#     else:
#         return render_template('admin/login.html')  # Render the login page for non-authenticated users
#
#
# # @app.route('/redirect_login', methods=['GET', 'POST'])
# # def redirect_login():
# #     return render_template('admin/login.html')
# #
# #
# # @app.route('/redirect_register', methods=['GET', 'POST'])
# # def redirect_register():
# #     return render_template('admin/register.html')

from flask import request, session, redirect, render_template, make_response
from base import app
from base.com.vo.login_vo import loginVO


# Define the logout route
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Remove the user's session data
    session.clear()
    # Redirect the user to the login page
    return redirect("/")


# Add cache control headers to prevent caching for all routes
@app.after_request
def add_cache_control(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect('/admin/load_dashboard')

    error = None  # Initialize error message

    if request.method == 'POST':
        un = request.form.get("userName")
        pwd = request.form.get("pw")

        # Query the database to check user credentials
        user = loginVO.query.filter_by(user_name=un, password=pwd).first()

        if user:
            session['logged_in'] = True
            app.logger.info(f"User {un} logged in successfully.")
            return redirect('/admin/load_dashboard')
        else:
            app.logger.error("Login failed. Invalid username or password.")
            error = 'Invalid username or password'

    return render_template('admin/login.html', error=error)  # Pass error message to the template


# Dashboard route
@app.route('/admin/load_dashboard')
def admin_load_dashboard():
    if session.get('logged_in'):
        return render_template('admin/index.html')
    else:
        return redirect('/')


# Index route
@app.route('/')
def hello_world():
    if session.get('logged_in'):
        return redirect('/admin/load_dashboard')  # Redirect authenticated users to the dashboard
    else:
        return render_template('admin/login.html')  # Render the login page for non-authenticated users
