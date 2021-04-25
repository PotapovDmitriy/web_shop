import ReactDOM from 'react-dom';
import React from 'react';
import axios from 'axios'
axios.defaults.headers.post['Authorization'] = 'JWT '+localStorage.getItem('jwt');
axios.defaults.headers.get['Authorization'] = 'JWT '+localStorage.getItem('jwt');
import 'boxicons'
import { BrowserRouter as Router, NavLink, Redirect, Route, Switch} from 'react-router-dom';

import styles from './style.css'
import Home from './pages/Home/Home.jsx'
import AddCategory from './pages/AddCategory/AddCategory.jsx';
import AddProduct from './pages/AddProduct/AddProduct.jsx';
import AllCategories from './pages/AllCategories/AllCategories.jsx';
import RedactCategory from './pages/RedactCategory/RedactCategory.jsx';
import RedactProduct from './pages/RedactProduct/RedactProduct.jsx';
import AllProducts from './pages/AllProducts/AllProducts.jsx';
import Login from './pages/Login/Login.jsx';
import Button from './components/Button/Button.jsx';

const API_GETEWAY_HOST = 'http://localhost:8060/';
function logout(){
    localStorage.removeItem('jwt');
    window.location.href = '/';
}

ReactDOM.render(
    <div className={styles.app}>
        <Router>
            <div className={styles.header}>
                <h1 className={styles.siteName}>Web Shop</h1>
                <h2 className={styles.siteDistrict}>Admin panel</h2>
                {(localStorage.getItem('jwt'))
                ?<div className={styles.logoutButton}>
                    <Button value='Logout' onClick={logout} bgColor='#d58520'/>
                </div>
                :null}
            </div>
            <nav className={styles.navigationBar}>
                <div className={styles.compareLinks}>
                    <NavLink className={styles.navLink} activeClassName={styles.navLinkActive} exact to='/'>
                        <p>Home</p>
                    </NavLink>
                    <NavLink className={styles.navLink} activeClassName={styles.navLinkActive} to='/new_category'>
                        <p>New category</p>
                    </NavLink>
                    <NavLink className={styles.navLink} activeClassName={styles.navLinkActive} to='/new_product'>
                        <p>New product</p>
                    </NavLink>
                    <NavLink className={styles.navLink} activeClassName={styles.navLinkActive} to='/all_categories'>
                        <p>All categories</p>
                    </NavLink>
                    <NavLink className={styles.navLink} activeClassName={styles.navLinkActive} to='/all_products'>
                        <p>All products</p>
                    </NavLink>
                </div>
            </nav>
            <Switch>
                <Route exact path='/' component={(localStorage.getItem('jwt'))?Home:Login}></Route>
                <Route exact path='/new_category' component={(localStorage.getItem('jwt'))?AddCategory:Login}></Route>
                <Route exact path='/new_product' component={(localStorage.getItem('jwt'))?AddProduct:Login}></Route>
                <Route exact path='/all_categories' component={(localStorage.getItem('jwt'))?AllCategories:Login}></Route>
                <Route exact path='/all_categories/:id' component={(props)=>(localStorage.getItem('jwt'))?<RedactCategory {...props}/>:<Login/>}></Route>
                <Route exact path='/all_products' component={(localStorage.getItem('jwt'))?AllProducts:Login}></Route>
                <Route exact path='/all_products/:id' component={(props)=>(localStorage.getItem('jwt'))?<RedactProduct {...props}/>:<Login/>}></Route>
            </Switch>
        </Router>
    </div>,
    document.getElementById("app")
)

export {API_GETEWAY_HOST}