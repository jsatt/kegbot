{
    applyMiddleware
    createStore
} = require 'redux'
thunk = require('redux-thunk').default

kegbotApp = require './reducers.cjsx'

store = createStore(
    kegbotApp
    applyMiddleware(thunk)
)

module.exports = store
