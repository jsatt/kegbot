React = require 'react'
ReactDOM = require 'react-dom'
Link = require('react-router').Link

TestComponent = (props) ->
        <div className='test-component col-xs-12'>
            <p>test</p>
            <Link to="/taps/123">to taps</Link>
            {props.children}
            {props.kegbot.testing}
            <button className="btn btn-primary" onClick=props.onAddClick>Add another</button>
            {props.kegbot.taps.map (tap) ->
                <div key={tap.id}>
                    <h2>{tap.beverage.name}</h2>
                    <ul>
                        <li>
                            <strong>Style</strong> <span>{tap.beverage.style}</span>
                        </li>
                        <li>
                            <strong>ABV</strong> <span>{tap.beverage.abv}</span>
                        </li>
                        <li>
                            <strong>Dispensed ml</strong> <span>{tap.dispensed_ml}</span>
                        </li>
                        <li>
                            <strong>Total ml</strong> <span>{tap.total_ml}</span>
                        </li>
                    </ul>
                </div>
            }
        </div>

module.exports = TestComponent
