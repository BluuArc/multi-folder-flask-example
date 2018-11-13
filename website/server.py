from flask import send_file, send_from_directory

# app is Flask instance from server.py in root
def extendApplication(app):
  # NOTE: all paths using current directory must be relative to the server.py file in the root repository
  @app.route('/website/')
  def websiteRootHandler():
    return send_file('website/index.html')

  @app.route('/website/static/<path:filename>')
  def websiteStaticAssetsHandler(filename):
    return send_from_directory('website/static', filename)

  @app.route('/website/api/members')
  def websiteApiMembersHandler():
    return send_file('website/apiMock/members.json')
