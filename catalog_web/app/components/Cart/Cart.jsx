import axios from 'axios';
import React, { Component } from 'react';
import { API_HOST } from '../../app.jsx';
import LoginForm from '../LoginForm/LoginForm.jsx';
import Button from './../Button/Button.jsx';
import styles from './style.css'

export default class Cart extends Component {
    constructor(props) {
        super(props);
        
        this.state ={
            open: false,
            loginForm : null,
            products : null,
            cart : null
        };

       this.cartOpen = this.cartOpen.bind(this);
       this.getCart = this.getCart.bind(this);
       this.addProduct = this.addProduct.bind(this);
       this.delProduct = this.delProduct.bind(this);
       this.delRow = this.delRow.bind(this);
    }
    getCart(){
        axios.get(API_HOST+'/cart')
            .then((res)=>{
                this.setState({
                    open : true,
                    products : res.data.products,
                    cart : res.data
                });
            })
            .catch((er)=>{
                console.log(er);
            });
    }
    cartOpen(){
        if(!localStorage.getItem('jwt')){
            this.setState({
                loginForm : <LoginForm close={()=>{this.setState({loginForm : null})}}/>
            });
        }
        else{
            this.getCart();
        }
    }

    addProduct(id){
        axios.get(API_HOST+'/add_product?product_id='+id, {withCredentials : true})
            .then((res)=>{
            })
            .catch((er)=>{
                console.log(er);
            })
    }

    delProduct(id){
        axios.get(API_HOST+'/product_minus_one?product_id='+id, {withCredentials : true})
            .then((res)=>{
            })
            .catch((er)=>{
                console.log(er);
            })
    }

    delRow(id){
        axios.get(API_HOST+'/delete_product?product_id='+id, {withCredentials : true})
            .then((res)=>{
            })
            .catch((er)=>{
                console.log(er);
            })
    }

    render() {
        return (
            <div className={styles.cart}>
                <div className={styles.cartButton}>
                    <Button value='Cart' onClick={this.cartOpen} bgColor='transparent'/>
                </div>
                {this.state.loginForm}
                {(this.state.open)
                ?<div>
                    {(this.state.products)
                    ?<div className={styles.cartWindow}>
                        <div className={styles.cartForm}>
                            <h3>CART</h3>
                            {this.state.products.map((product)=>{
                            return <div key={product.product_id} style={{border : 1+'px solid #000'}}>
                                    <p>Name :{product.name}</p>
                                    <p>Price:{product.price}</p>
                                    <p>Count: {product.count}</p>
                                    <button onClick={(e)=>{
                                        this.addProduct(product.product_id);
                                    }}>+</button>
                                    <button onClick={()=>{
                                        this.delProduct(product.product_id);
                                    }}>-</button>
                                    {/* <button onClick={()=>{
                                        this.delRow(product.product_id);
                                    }}>Delete</button> */}
                                </div>
                            })}
                            <p>Final price: {this.state.cart.full_price}¥</p>
                            <button>Заказать</button>
                            <button onClick={()=>{this.setState({open : false})}}>Close</button>
                        </div>

                    </div>
                    :null}
                </div>
                :null}
                
            </div>
        )
    }
}
