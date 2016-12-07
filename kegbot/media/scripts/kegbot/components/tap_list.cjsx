React = require 'react'
ReactDOM = require 'react-dom'
{Component} = require 'react'
{connect} = require 'react-redux'
{Link} = require 'react-router'
Helmet = require 'react-helmet'

actions = require '../actions.cjsx'
Tap = require './tap.cjsx'

mapStateToProps = (state) ->
    taps: state.kegbot.taps

mapDispatchToProps = (dispatch) ->
    loadTaps: -> dispatch actions.makeQuery()

class TapListComponent extends Component
    componentWillMount: ->
        @props.loadTaps()
    render: ->
        <div id="tap-list">
            <Helmet title="Taps" />
            {for tap in @props.taps
                <Link to="/taps/#{tap.id}" key=tap.id>
                    <Tap tap=tap />
                </Link>
            }
        </div>

TapListComponent.defaultProps =
    title: 'Taps'
module.exports = connect(mapStateToProps, mapDispatchToProps)(TapListComponent)
