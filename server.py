import hashlib
import os
from dotenv import load_dotenv
from flask import Flask, render_template, session, request, flash, redirect, url_for
from login import LoginForm
from flask_gravatar import Gravatar
import ldclient
from ldclient.config import Config

app = Flask(__name__, static_folder='public', template_folder='views')
app.config['SECRET_KEY'] = 'you will never guess'
gravatar = Gravatar(app, default='robohash')

load_dotenv()
LD_SDK_KEY = os.getenv('LD_SDK_KEY')
print("print key", LD_SDK_KEY)
ldclient.set_config(Config(LD_SDK_KEY))
# This will be the actual LaunchDarkly client we use from this point on
ld_client = ldclient.get()

@app.route('/')
def pricing():
    """Displays the pricing page."""
    ## Fetch the user's email address. If they aren't logged in,
    ## the stored value will be None.
    email = session.get("email")
    if (email):
      user = user_object_from_email(email)
    else:
      ## Since the user isn't logged in,
      ## let's tell LD that this is an anonymous user.
      user = {
        "key": "anon",
        "anonymous": True
      }
    is_tier_3_enabled = ld_client.variation('pricing-tier-3', user, False)
    return render_template(
      'pricing.html',
      is_tier_3_enabled=is_tier_3_enabled,
      email=email,
      key=user['key']
    )

def user_object_from_email(email):
    ## Hash the email address using the SHA256 algorithm
    email_hash = hashlib.sha256(email.encode())
    ## Output the hash as hexadecimal and truncate to 10 characters long
    email_hash_hex = email_hash.hexdigest()[:10]
    ## Identify user by their hashed email address
    return {
      "key": email_hash_hex
    }

  
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Displays the login page."""
    form = LoginForm(request.form)
    if form.validate_on_submit():
      session["email"] = form.email.data
      return redirect(url_for("pricing"))
    
    return render_template('login.html', form=form)

  
@app.route('/logout')
def logout():
    """Displays the logout page."""
    session.pop("email")
    return redirect(url_for("pricing"))
  
if __name__ == '__main__':
    app.run()