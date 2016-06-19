types = require './action_types.cjsx'

actions =
    addToTest: ->
        type: types.TEST_ACTIONS

    startQuery: ->
        type: types.START_QUERY
    finishQuery: (results) ->
        type: types.FINISH_QUERY
        payload: results
    makeQuery: ->
        (dispatch) ->
            dispatch actions.startQuery()
            fetch('/api/taps/').then( (resp) ->
                resp.json()
            ).then( (data) ->
                dispatch actions.finishQuery(data)
            )

module.exports = actions
