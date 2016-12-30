React = require 'react'
ReactDOM = require 'react-dom'
{Component} = require 'react'

class Tap extends Component
    render: ->
        <div className="tap">{@props.tap.beverage.name}
            <div className="level-container">
                <div className="level" data-level=@props.tap.current_level></div>
            </div>
        </div>
module.exports = Tap
