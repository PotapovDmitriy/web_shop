import React, { Component } from 'react'
import axios from 'axios'

import styles from './style.css'
import Button from '../../components/Button/Button.jsx';
import Load from '../../components/Load/Load.jsx';
import {API_GETEWAY_HOST} from './../../app.jsx'

export default class AllProducts extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            products : undefined
        };

        this.getProducts = this.getProducts.bind(this);
        this.deleteProducts = this.deleteProducts.bind(this);
    }
    
    componentDidMount(){
        this.getProducts();
    }

    getProducts(){
        axios.get(API_GETEWAY_HOST+'products', {withCredentials:true})
        .then((res)=>{
            this.setState({
                products :res.data.products
            });
        })
        .catch((er)=>{
            console.log(er);
        });
    }

    deleteProducts(id){
        axios.get(API_GETEWAY_HOST+'delete_product?id='+id, {withCredentials:true})
        .then(()=>{
            console.log('Product delete');
            this.getProducts();
        })
        .catch((er)=>{
            console.log(er);
        });
    }

    render() {
        return (
            <div>
                {(this.state.products)
                ?<div className={styles.allProducts}>
                    {this.state.products.map((product)=>{
                        return <div key={product.product_id} className={styles.oneProduct}>
                                    <div className={styles.productsInfo}>
                                        <img src={product.image_url} className={styles.productImage}></img>
                                        <div className={styles.productText}>
                                            <p className={styles.textBlock}><b>Name: </b>{product.name}</p>
                                            <p className={styles.textBlock}><b>Category: </b>{product.category_name}</p>
                                            <p className={styles.textBlock}><b>Specifications: </b>{product.characteristic}</p>
                                            <p className={styles.textBlock}><b>Description: </b>{product.summary}</p>
                                        </div>
                                    </div>
                                    <div className={styles.productPriceAndButtons}>
                                        <p className={styles.priceText}>Price: <span>{product.price} ¥</span></p>
                                        <div className={styles.buttons}>
                                            <Button value='Edit' bgColor='#d58520' onClick={()=>{
                                                const { history } = this.props;
                                                history.push('/all_products/'+product.product_id);}}/>
                                            <Button value='Delete' bgColor='#f44336' onClick={(e)=>{this.deleteProducts(product.product_id,e)}}/>
                                        </div>
                                    </div>
                                </div>
                    })}
                </div>
                :<Load/>}
            </div>
        )
    }
}
