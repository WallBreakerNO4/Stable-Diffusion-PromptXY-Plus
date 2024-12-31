from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # 注册路由
    from app import routes
    app.register_blueprint(routes.main)
    
    return app 