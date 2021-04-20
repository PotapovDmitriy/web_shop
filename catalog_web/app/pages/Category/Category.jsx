import React, { Component } from 'react'
import axios from 'axios'

import {API_HOST} from '../../app.jsx'
import styles from './style.css'
import Load from '../../components/Load/Load.jsx';
import { Link } from 'react-router-dom';
import LoginForm from '../../components/LoginForm/LoginForm.jsx';

export default class Category extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            category : undefined,
            loginForm : null,
            cart : []
        };

        this.addToCart = this.addToCart.bind(this);
    }
    

    componentDidMount(){
        axios.get(API_HOST+'/category?id='+this.props.match.params.id, {withCredentials : true})
        .then((res)=>{
            this.setState({
                category : res.data
            });
        })
        .catch((er)=>{
            console.log(er);
        })
    }

    addToCart(id){
        if(!localStorage.getItem('jwt')){
            this.setState({
                loginForm : <LoginForm close={()=>{this.setState({loginForm:null})}}/>
            })
        }
        else{
            axios.get(API_HOST+'/add_product?product_id='+id, {withCredentials : true})
            .then((res)=>{
                let cart = this.state.cart;
                cart.push(id);
                this.setState({
                    cart : cart
                });
            })
            .catch((er)=>{
                console.log(er);
            })
        }
    }

    render() {
        return (
            <div>
                <Link to='/' className={styles.homeLink}>Home</Link>
                {this.state.loginForm}
                {(this.state.category)
                ?<div>
                    <h3 className={styles.h3}>{this.state.category.name}</h3>
                    <div>
                        {(this.state.category.isNil)
                        ?<div className={styles.childrenProducts}>
                            {(this.state.category.children.length === 0)
                            ?<p className={styles.noChildren}>This category has no products</p>
                            :null}
                            {this.state.category.children.map((product)=>{
                                return <div key={product.product_id} className={styles.product}>
                                            <div className={styles.flex}>
                                                <img src={product.image_url} className={styles.img}></img>
                                                <div className={styles.description}>
                                                    <p>{product.name}</p>
                                                    <p>{product.characteristic}</p>
                                                    <p>{product.summary}</p>
                                                </div>
                                            </div>
                                            {(!this.state.cart.includes(product.product_id))
                                            ?<button className={styles.button} onClick={()=>{this.addToCart(product.product_id)}}>Add to cart</button>
                                            :<button className={styles.button}>IN CART</button>}
                                            
                                        </div>
                            })}
                        </div>
                        :<div className={styles.childrenCategories}>
                            {(this.state.category.children.length === 0)
                            ?<p className={styles.noChildren}>This category has no subcategories</p>
                            :null}
                            {this.state.category.children.map((category)=>{
                                return <a key={category.category_id} href={'/category/'+category.category_id} className={styles.link}>{category.name}</a>
                            })}
                        </div>}
                    </div>
                </div>
                :<Load/>}
            </div>
        )
    }
}
