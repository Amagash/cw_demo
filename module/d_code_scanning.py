from flask import app


@app.route('/redirect')
def redirect_url_noncompliant():
    from flask import request, redirect
    endpoint = request.args['url']
    # Noncompliant: redirect to a user-supplied URL without sanitization.
    return redirect(endpoint)