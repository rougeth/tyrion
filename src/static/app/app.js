import React from 'react';
import ReactDOM from 'react-dom';
import {Router, Route, browserHistory} from 'react-router';


class App extends React.Component {
  render() {
    return <h1>Hello, Tyrion!</h1>;
  }
};

ReactDOM.render((
  <Router history={browserHistory}>
    <Route path='/' component={App} />
  </Router>
), document.querySelector('#app'));
