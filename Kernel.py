from masonite.foundation import response_handler
from cleo import Application as CommandApplication
from masonite.storage import StorageCapsule
from masonite.auth import Sign
import os
from masonite.environment import LoadEnvironment
from masonite.utils.structures import load, load_routes
from masonite.middleware import (
    SessionMiddleware,
    EncryptCookies,
    VerifyCsrfToken,
    LoadUserMiddleware,
)
from masonite.routes import Route


from app.middlware.VerifyCsrfToken import VerifyCsrfToken


class Kernel:

    http_middleware = [
        EncryptCookies
    ]

    route_middleware = {
        "web": [
            SessionMiddleware, 
            LoadUserMiddleware, 
            VerifyCsrfToken
        ],
    }
    
    def __init__(self, app):
        self.application = app

    def register(self):
        # Register routes
        self.load_environment()
        self.register_configurations()
        self.register_middleware()
        self.register_routes()
        self.register_database()
        self.register_templates()
        self.register_storage()

    def load_environment(self):
        LoadEnvironment()

    def register_routes(self):
        Route.set_controller_module_location('app.controllers')

        self.application.make('router').add(
            Route.group(
                load_routes("routes.web"), middleware=["web"]
            )
        )

    def register_middleware(self):
        self.application.make('middleware').add(self.route_middleware).add(self.http_middleware)

    def register_configurations(self):
        self.application.bind("config.location", "app/config")
        self.application.bind("config.application", "config.application")
        self.application.bind("config.mail", "config.mail")
        self.application.bind("config.session", "config.session")
        self.application.bind("config.queue", "config.queue")
        self.application.bind("config.database", "config.database")
        self.application.bind("config.cache", "config.cache")
        self.application.bind("config.broadcast", "config.broadcast")
        self.application.bind("config.auth", "config.auth")
        self.application.bind("config.filesystem", "config.filesystem")
        self.application.bind("config.notification", "config.notification")

        self.application.bind("base_url", "http://localhost:8000")

        self.application.bind("jobs.location", "app/jobs")
        self.application.bind("controller.location", "app.controllers")
        self.application.bind("providers.location", "app/providers")
        self.application.bind("mailables.location", "app/mailables")
        self.application.bind("listeners.location", "app/listeners")
        self.application.bind("validation.location", "app/validation")
        self.application.bind(
            "server.runner", "masonite.commands.ServeCommand.main"
        )

        key = load(self.application.make("config.application")).KEY
        self.application.bind("key", key)
        self.application.bind("sign", Sign(key))


    def register_templates(self):
        self.application.bind("views.location", "templates/")

    def register_storage(self):
        storage = StorageCapsule(self.application.base_path)
        storage.add_storage_assets(
            {
                # folder          # template alias
                "app/storage/static": "static/",
                "app/storage/compiled": "static/",
                "app/storage/uploads": "static/",
                "app/storage/public": "/",
            }
        )
        self.application.bind("storage_capsule", storage)

    def register_database(self):
        from masoniteorm.query import QueryBuilder

        self.application.bind(
            "builder",
            QueryBuilder(
                connection_details=load(
                    self.application.make("config.database")
                ).DATABASES
            ),
        )

        self.application.bind("migrations.location", "app/databases/migrations")
        self.application.bind("seeds.location", "app/databases/seeds")

        from config.database import DB

        self.application.bind("resolver", DB)

    def register_storage(self):
        storage = StorageCapsule(self.application.base_path)
        storage.add_storage_assets(
            {
                # folder          # template alias
                "storage/static": "static/",
                "storage/compiled": "static/",
                "storage/uploads": "static/",
                "storage/public": "/",
            }
        )
        self.application.bind("storage_capsule", storage)

        self.application.set_response_handler(response_handler)
        self.application.use_storage_path(
            os.path.join(self.application.base_path, "storage")
        )
