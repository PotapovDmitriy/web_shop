import ReactDOM from 'react-dom';
import React from 'react';
import axios from 'axios'
axios.defaults.headers.post['Authorization'] = 'JWT '+localStorage.getItem('jwt');
axios.defaults.headers.get['Authorization'] = 'JWT '+localStorage.getItem('jwt');
import styles from './style.css'
import { BrowserRouter as Router, NavLink, Redirect, Route, Switch} from 'react-router-dom';

import Home from './pages/Home/Home.jsx'
import Category from './pages/Category/Category.jsx';
import Cart from './components/Cart/Cart.jsx';

const API_HOST = 'http://localhost:8060';

ReactDOM.render(
    <div className={styles.app}>
        {(localStorage.getItem('jwt'))
        ?<button className={styles.logoutButton} onClick={()=>{
            localStorage.removeItem('jwt');
            console.log('ddd');
            window.location.href = '/';
        }}>LOGOUT</button>
        :null}
        
        <Cart/>
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