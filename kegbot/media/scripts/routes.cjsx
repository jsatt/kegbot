Provider = require('react-redux').Provider
React = require 'react'
Route = require('react-router').Route
Router = require('react-router').Router
browserHistory = require('react-router').browserHistory
syncHistoryWithStore = require('react-router-redux').syncHistoryWithStore

Taps = require './taps/components.cjsx'
TestContainer = require './kegbot/containers.cjsx'
store = require './store.cjsx'

history = syncHistoryWithStore(browserHistory, store)

routes =
    <Provider store=store>
        <Router history={history}>
            <Route path="/" component=TestContainer>
                <Route path="taps/:id" component={Taps}></Route>
            </Route>
        </Router>
    </Provider>

module.exports = routes

