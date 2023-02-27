# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound

# App modules
from apps import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):

    try:

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template( 'pages/index.html' + path, segment=segment )
    
    except TemplateNotFound:
        return render_template('pages/index.html'), 404


# Pages
@app.route('/pages/about/')
def pages_about():
  return render_template('pages/about.html', segment='about', parent='pages')

@app.route('/pages/contact/')
def pages_contact():
  return render_template('pages/contact.html', segment='contact', parent='pages')

@app.route('/pages/blank/')
def pages_blank():
  return render_template('pages/blank.html', segment='blank-page', parent='pages')

@app.route('/pages/landing-freelancer/')
def pages_landing_freelancer():
  return render_template('pages/landing-freelancer.html', segment='landing-freelancer', parent='pages') 

# Accounts 
@app.route('/accounts/sign-in/')
def acc_sign_in():
  return render_template('accounts/sign-in.html', segment='sign-in', parent='accounts')

@app.route('/accounts/sign-up/')
def acc_sign_up():
  return render_template('accounts/sign-up.html', segment='sign-up', parent='accounts')

@app.route('/accounts/password-change/')
def acc_change_password():
  return render_template('accounts/password_change.html', segment='password-change', parent='accounts')

@app.route('/accounts/password-change-complete/')
def acc_password_change_complete():
  return render_template('accounts/password_change_done.html', segment='password-change', parent='accounts')  

@app.route('/accounts/password-reset/')
def acc_password_reset():
  return render_template('accounts/password_reset.html', segment='password-reset', parent='accounts')  

@app.route('/accounts/password-reset-done/')
def acc_password_reset_done():
  return render_template('accounts/password_reset_done.html', segment='password-reset-done', parent='accounts')  

@app.route('/accounts/password-reset-confirm/')
def acc_password_reset_confirm():
  return render_template('accounts/password_reset_confirm.html', segment='password-reset-confirm', parent='accounts')

@app.route('/accounts/password-reset-complete/')
def acc_password_reset_complete():
  return render_template('accounts/password_reset_complete.html', segment='password-reset-complete', parent='accounts')

# Components
@app.route('/components/accordions/')
def components_accordions():
  return render_template('components/accordions.html', segment='accordions', parent='components')

@app.route('/components/alerts/')
def components_alerts():
  return render_template('components/alerts.html', segment='alerts', parent='components')

@app.route('/components/badges/')
def components_badges():
  return render_template('components/badges.html', segment='badges', parent='components')

@app.route('/components/bootstrap-carousels/')
def components_bs_carousels():
  return render_template('components/bootstrap-carousels.html', segment='bootstrap-carousels', parent='components')

@app.route('/components/breadcrumbs/')
def components_breadcrumbs():
  return render_template('components/breadcrumbs.html', segment='breadcrumbs', parent='components')    

@app.route('/components/buttons/')
def components_buttons():
  return render_template('components/buttons.html', segment='buttons', parent='components')

@app.route('/components/cards/')
def components_cards():
  return render_template('components/cards.html', segment='cards', parent='components')

@app.route('/components/dropdowns/')
def components_dropdowns():
  return render_template('components/dropdowns.html', segment='dropdowns', parent='components')

@app.route('/components/forms/')
def components_forms():
  return render_template('components/forms.html', segment='forms', parent='components')

@app.route('/components/modals/')
def components_modals():
  return render_template('components/modals.html', segment='modals', parent='components')

@app.route('/components/navs/')
def components_navs():
  return render_template('components/navs.html', segment='navs', parent='components')

@app.route('/components/pagination/')
def components_pagination():
  return render_template('components/pagination.html', segment='pagination', parent='components')

@app.route('/components/popovers/')
def components_popovers():
  return render_template('components/popovers.html', segment='popovers', parent='components')

@app.route('/components/progress-bars/')
def components_progress_bars():
  return render_template('components/progress-bars.html', segment='progress-bars', parent='components')

@app.route('/components/tables/')
def components_tables():
  return render_template('components/tables.html', segment='tables', parent='components')

@app.route('/components/tabs/')
def components_tabs():
  return render_template('components/tabs.html', segment='tabs', parent='components')

@app.route('/components/toasts/')
def components_toasts():
  return render_template('components/toasts.html', segment='toasts', parent='components')

@app.route('/components/tooltips/')
def components_tooltips():
  return render_template('components/tooltips.html', segment='tooltips', parent='components')

@app.route('/components/typography/')
def components_typography():
  return render_template('components/typography.html', segment='typography', parent='components')                  

def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
