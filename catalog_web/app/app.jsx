import ReactDOM from 'react-dom';
import React from 'react';
import styles from './style.css'
import { BrowserRouter as Router, NavLink, Redirect, Route, Switch} from 'react-router-dom';

import Home from './pages/Home/Home.jsx'
import Category from './pages/Category/Category.jsx';

const API_HOST = 'http://localhost:8020'

ReactDOM.render(
    <div className={styles.app}>
        <Router>
            <Switch>
                <Route exact path='/' component={Home}></Route>
                <Route exact path='/category/:id' component={Category}></Route>
            </Switch>
        </Router>
    </div>,
    document.getElementById("app")
)

export {API_HOST}