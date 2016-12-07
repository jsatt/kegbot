React = require 'react'
ReactDOM = require 'react-dom'
Helmet = require 'react-helmet'

TapsComponent = React.createClass
    render: ->
        <div className="test-component">
            <Helmet title="specific taps" />
            <p>home {@props.params.id}</p>
        </div>

module.exports = TapsComponent

