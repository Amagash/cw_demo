from flask import app


@app.route('/redirect')
def redirect_url_noncompliant():
    from flask import request, redirect
    endpoint = request.args['url']
    return redirect(endpoint)