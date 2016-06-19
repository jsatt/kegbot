render = require('react-dom').render

routes = require './routes.cjsx'

render routes, document.getElementById 'app'
