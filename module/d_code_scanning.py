from flask import app


@app.route('/redirect')
def redirect_url_noncompliant():
    from flask import request, redirect
    endpoint = request.args['url']
    if validators.url(endpoint):  # import validators
        return redirect(endpoint)
    else:
        raise RuntimeError("URL being redirected to is invalid.")