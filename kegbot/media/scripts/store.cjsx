applyMiddleware = require('redux').applyMiddleware
createStore = require('redux').createStore
thunk = require('redux-thunk').default

kegbotApp = require './reducers.cjsx'

store = createStore(
    kegbotApp
    applyMiddleware(thunk)
)

module.exports = store
