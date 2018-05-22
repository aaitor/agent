import hug

from agent.core.AssetsManager import AssetsManager
from agent.server.rest.resources.AbstractResource import AbstractResource


@hug.object.urls()
class AssetsResource(AbstractResource):
    URL_PREFIX = '/assets'
    RESOURCE_URL = '/metadata'


    def __init__(self):
        AbstractResource.__init__(self)


    @hug.object.get('/metadata/{asset_id}')
    def get(self, response, asset_id):
        manager = AssetsManager()
        return manager.register(asset_id)
