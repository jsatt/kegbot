React = require 'react'
ReactDOM = require 'react-dom'
{Component} = require 'react'
{connect} = require 'react-redux'

actions = require '../actions.cjsx'

mapStateToProps = (state) ->
    taps: state.kegbot.taps

mapDispatchToProps = (dispatch) ->
    loadTaps: -> dispatch actions.makeQuery()

class TapListComponent extends Component
    componentWillMount: ->
        @props.loadTaps()
    render: ->
        console.log 'render', this, arguments
        <div id="tap-list">
            <ol>
            {for tap in @props.taps
                <li key=tap.beverage.id>{tap.beverage.name}</li>
            }
            </ol>
        </div>

module.exports = connect(mapStateToProps, mapDispatchToProps)(TapListComponent)
