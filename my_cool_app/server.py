from flask import send_file, send_from_directory

# app is Flask instance from server.py in root
def extendApplication(app):
  # NOTE: all paths using current directory must be relative to the server.py file in the root repository
  @app.route('/my_cool_app/')
  def appRootHandler():
    return send_file('my_cool_app/index.html')

  @app.route('/my_cool_app/static/<path:filename>')
  def appStaticAssetsHandler(filename):
    return send_from_directory('my_cool_app/static', filename)

  @app.route('/my_cool_app/api/members')
  def appApiMembersHandler():
    return send_file('my_cool_app/apiMock/members.json')
