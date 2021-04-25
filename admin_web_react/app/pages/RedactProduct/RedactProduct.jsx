import React, { Component } from 'react'
import axios from 'axios';
import classnames from 'classnames'

import styles from './style.css'
import Input from '../../components/Input/Input.jsx';
import Textarea from '../../components/Textarea/Textarea.jsx';
import Button from '../../components/Button/Button.jsx';
import Load from '../../components/Load/Load.jsx';
import {API_GETEWAY_HOST} from './../../app.jsx'

export default class RedactProduct extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            product : undefined,
            newProductName : '',
            newPrice : '',
            newDescription : '',
            newSpecification : '',
            newImage : ''
        };

        this.updateProduct = this.updateProduct.bind(this);
    }
    
    componentDidMount(){
        axios.get(API_GETEWAY_HOST +'product?id='+ this.props.match.params.id, {withCredentials:true})
        .then((res)=>{
            this.setState({
                product : res.data,
                newProductName : res.data.name,
                newPrice : res.data.price,
                newDescription : res.data.summary,
                newSpecification : res.data.characteristic,
                newImage : res.data.image_url
            });
            console.log(res.data);
        })
        .catch((er)=>{
            console.log(er);
        });
    }

    updateProduct(){
        if(this.state.newProductName === '' || this.state.newDescription === '' || 
        this.state.newSpecification === ''|| this.state.newImage === '' || this.state.newPrice === ''){
        this.setState({
            errorClass : styles.error
        });
        let timeout = setTimeout(()=>{
            this.setState({
                errorClass : undefined
            });
            clearTimeout(timeout);
        }, 2000);
    } else{
        let data = {
            name : this.state.newProductName,
            category_id : this.state.product.category_id,
            summary : this.state.newDescription,
            characteristic : this.state.newSpecification,
            image_url : this.state.newImage,
            price : this.state.newPrice,
            product_id : this.state.product.product_id
        };
        console.log(data);
        axios.post(API_GETEWAY_HOST+'redact_product', data, {withCredentials:true})
        .then((res)=>{
            const { history } = this.props;
            history.push('/all_products');
            console.log(res);
        })
        .catch((er)=>{
            console.log(er);
        })
    }
    }

    render() {
        return (
            <div>
                {(this.state.product)
                ?<div className={styles.addProduct}>
                    <h2 className={styles.h2}>Redact product</h2>
                    <Input placeholder='Input product name' 
                        label='Product name' 
                        id='#product_name' 
                        value={this.state.newProductName}
                        onChange={(e)=>{this.setState({ newProductName : e.target.value})}}
                        className={this.state.errorClass}/>
                    <br></br>
                    <Input placeholder='Input product price' 
                        label='Product price' 
                        id='#product_price'
                        value={this.state.newPrice}
                        onChange={(e)=>{this.setState({ newPrice : e.target.value})}}
                        className={this.state.errorClass}
                        type='number'/>
                    <div className={styles.categoryBlock}>
                        <p className={classnames(styles.description, this.state.errorClass)}>Category</p>
                        <p className={styles.choosenCategory}>{this.state.product.category_name}</p>
                    </div>
                    <Textarea className={this.state.errorClass} 
                    placeholder='Input description' 
                    label='Description' 
                    id='#description'
                    value={this.state.newDescription}
                    onChange={(e)=>{this.setState({newDescription : e.target.value})}}/>    
                    <Textarea className={this.state.errorClass} 
                    placeholder='Input specifications' 
                    label='Specifications' 
                    id='#specifications'
                    value={this.state.newSpecification}
                    onChange={(e)=>{this.setState({newSpecification : e.target.value})}}/>
                    <div className={styles.imageBlock}>
                        <Input placeholder='Input image url' 
                        label='Image' 
                        className={this.state.errorClass}
                        value={this.state.newImage}
                        onChange={(e)=>{this.setState({ newImage : e.target.value})}}/>
                        <img src={this.state.newImage} className={styles.img}></img>
                    </div>
                    <Button value='Save' onClick={this.updateProduct} bgColor='#d58520'></Button>
                </div>
                :<Load/>}
            </div>
        )
    }
}
