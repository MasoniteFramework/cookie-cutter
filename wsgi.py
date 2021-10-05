from masonite.foundation import Application, Kernel
from config.providers import PROVIDERS
from Kernel import Kernel as ApplicationKernel
import os


"""Start The Application Instance."""
application = Application(os.getcwd())

"""Now Bind important providers needed to make the framework work."""
application.register_providers(Kernel, ApplicationKernel)

"""Now Bind important application specific providers needed to make the application work."""
application.add_providers(*PROVIDERS)
