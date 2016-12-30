React = require 'react'
Helmet = require 'react-helmet'


class MainLayout extends React.Component
    render: (props) ->
        <div className="container-fluid">
            <Helmet titleTemplate="Kegbot | %s" defaultTitle="Kegbot" />
            <div className="row">
                <header className="col-12">Header stuff will go here</header>
                <article className="col-12">
                    {@props.children}
                </article>
                <footer className="col-12">footer if I need one</footer>
            </div>
        </div>


module.exports = MainLayout
