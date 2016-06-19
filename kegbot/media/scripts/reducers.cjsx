combineReducers = require('redux').combineReducers
routerReducer = require('react-router-redux').routerReducer

kegbot = require './kegbot/reducers.cjsx'

reducers = combineReducers
    kegbot: kegbot
    routing: routerReducer

module.exports = reducers
