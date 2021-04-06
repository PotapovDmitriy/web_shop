import ReactDOM from 'react-dom';
import React from 'react';
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
 
ReactDOM.render(
    <div className={styles.app}>
        <Router>
            <div className={styles.header}>
                <h1 className={styles.siteName}>Web Shop</h1>
                <h2 className={styles.siteDistrict}>Admin panel</h2>
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
                <Route exact path='/' component={Home}></Route>
                <Route exact path='/new_category' component={AddCategory}></Route>
                <Route exact path='/new_product' component={AddProduct}></Route>
                <Route exact path='/all_categories' component={AllCategories}></Route>
                <Route exact path='/all_categories/:id' component={(props)=><RedactCategory {...props}/>}></Route>
                <Route exact path='/all_products' component={AllProducts}></Route>
                <Route exact path='/all_products/:id' component={(props)=><RedactProduct {...props}/>}></Route>
            </Switch>
        </Router>
    </div>,
    document.getElementById("app")
)