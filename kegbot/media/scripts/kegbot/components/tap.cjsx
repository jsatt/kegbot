React = require 'react'
ReactDOM = require 'react-dom'
{Component} = require 'react'

class Tap extends Component
    render: ->
        <div>{@props.tap.beverage.name}</div>
module.exports = Tap
