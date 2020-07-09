import quart

def create_app():
    app = quart.Quart(__name__)
    @app.route("/")
    async def index():
        return "Hello World!"
    return app


if __name__ == "__main__":
    create_app().run()
