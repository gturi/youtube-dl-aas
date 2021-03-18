from src.restx_config import api
from src.service.downloader_service import DownloaderService
from flask_restx import Resource, fields

ns = api.namespace('youtube-dl', description='Download operations')

download = api.model('Download', {
    'urls': fields.List(fields.String(), required = True),
    'ydlOpts': fields.Wildcard(fields.String(), required = False)
})

@ns.route('/download')
class Download(Resource):
    '''TODO'''

    __downloader_service = DownloaderService()

    @ns.doc('downloads videos on filesystem', responses={
        200: 'Success',
        400: 'Validation Error'
    })
    @ns.expect(download)
    @ns.response(200, 'Success', fields.List(fields.String(example="/path/to/downloaded/file")))
    def post(self):
        body = api.payload
        urls = set(body.get('urls'))
        ydl_opts = body.get('ydlOpts', None)

        return self.__downloader_service.download(urls, ydl_opts)
