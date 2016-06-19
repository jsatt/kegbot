React = require 'react'
ReactDOM = require 'react-dom'

TapsComponent = React.createClass
    render: ->
        <div className='test-component'>
            <p>home {@props.params.id}</p>
        </div>

module.exports = TapsComponent

