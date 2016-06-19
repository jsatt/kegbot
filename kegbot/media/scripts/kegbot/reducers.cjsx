types = require './action_types.cjsx'

initial_state =
    taps: []
    testing: 0
    loading: false

kegbot = (state=initial_state, action) ->
    changes = switch action.type
        when types.TEST_ACTIONS
            val = state.testing + 1

            testing: val
        when types.START_QUERY
            loading: true
        when types.FINISH_QUERY
            loading: false
            taps: action.payload
        else
            {}
    Object.assign {}, state, changes

module.exports = kegbot
