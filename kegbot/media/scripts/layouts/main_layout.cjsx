React = require 'react'


MainLayout = React.createClass
    propTypes:
        title: React.PropTypes.string
    componentDidMount: ->
        document.title = this.props.title
    render: (props) ->
        <div className="row">
            <header className="col-xs-12">Header stuff will go here</header>
            <article className="col-xs-12">
                {@props.children}
            </article>
            <footer className="col-xs-12">footer if I need one</footer>
        </div>


module.exports = MainLayout
