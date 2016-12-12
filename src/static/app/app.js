import React from 'react';
import ReactDOM from 'react-dom';
import {Router, Route, browserHistory} from 'react-router';

import Home from './home';

ReactDOM.render((
  <Router history={browserHistory}>
    <Route path='/' component={Home} />
  </Router>
), document.querySelector('#app'));
