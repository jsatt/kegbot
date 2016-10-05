React = require 'react'
{Provider} = require 'react-redux'
{
    IndexRoute
    Route
    Router
} = require 'react-router'
{browserHistory} = require 'react-router'
{syncHistoryWithStore} = require 'react-router-redux'

Taps = require './taps/components.cjsx'
TapList = require './kegbot/components/tap_list.cjsx'
MainLayout = require './layouts/main_layout.cjsx'
store = require './store.cjsx'

history = syncHistoryWithStore(browserHistory, store)

routes =
    <Provider store=store>
        <Router history={history}>
            <Route path="/" component=MainLayout>
                <IndexRoute component=TapList />
                <Route path="taps/:id" component={Taps}></Route>
            </Route>
        </Router>
    </Provider>

module.exports = routes

