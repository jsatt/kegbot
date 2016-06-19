connect = require('react-redux').connect
TestComponent = require './components/test_component.cjsx'
actions = require './actions.cjsx'

mapStateToProps = (state) ->
    kegbot: state.kegbot

mapDispatchToProps = (dispatch) ->
    onAddClick: ->
        dispatch actions.makeQuery()

TestContainer = connect(mapStateToProps, mapDispatchToProps)(TestComponent)

module.exports = TestContainer
