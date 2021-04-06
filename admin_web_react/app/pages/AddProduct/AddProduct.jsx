import React, { Component } from 'react';
import axios from 'axios';
import classnames from 'classnames'

import styles from './style.css';
import Load from '../../components/Load/Load.jsx';
import Input from '../../components/Input/Input.jsx';
import Button from '../../components/Button/Button.jsx';
import Textarea from '../../components/Textarea/Textarea.jsx';

export default class AddProduct extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            categories : undefined,
            choosenCategory : undefined,
            categoriesClass : styles.hidden,
            errorClass : undefined,
            productName : '',
            productSpecifications : '',
            productDescription : '',
            productImage : '',
            productPrice : ''
        };

        this.createProduct = this.createProduct.bind(this);
    }

    componentDidMount(){
        axios.get('http://localhost:8010/categories', {withCredentials:true})
        .then((res)=>{
            this.setState({
                categories : res.data.categories.filter((category)=>{
                    return category.isNil;
                })
            });
        })
        .catch((er)=>{
            console.log(er);
            this.setState({
                categories: [{category_id : 1, name : 'first'},{category_id : 2, name : 'second'}]
            })
        });
    }

    createProduct(){
        if(this.state.productName === '' || this.state.productDescription === '' || 
            this.state.productSpecifications === '' || !this.state.choosenCategory || this.state.productImage === '' || this.state.newPrice === ''){
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
                name : this.state.productName,
                category_id : this.state.choosenCategory.category_id,
                summary : this.state.productDescription,
                characteristic : this.state.productSpecifications,
                image_url : this.state.productImage,
                price : this.state.productPrice
            };
            console.log(data);
            axios.post('http://localhost:8010/new_product', data, {withCredentials:true})
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
                {(this.state.categories)
                ?<div className={styles.addProduct}>
                    <h2 className={styles.h2}>Add product</h2>
                    <Input placeholder='Input product name' 
                        label='Product name' 
                        id='#product_name' 
                        onChange={(e)=>{this.setState({ productName : e.target.value})}}
                        className={this.state.errorClass}/>
                    <br></br>
                    <Input placeholder='Input product price' 
                        label='Product price' 
                        id='#product_price' 
                        onChange={(e)=>{this.setState({ productPrice : e.target.value})}}
                        className={this.state.errorClass}
                        type='number'/>
                    <div className={styles.categoryBlock}>
                        <p className={classnames(styles.description, this.state.errorClass)}>Category</p>
                        {(this.state.choosenCategory)
                        ?<p className={styles.choosenCategory} 
                            onClick={()=>{
                                this.setState({
                                    categoriesClass : (this.state.categoriesClass === styles.hidden)?styles.categories:styles.hidden
                                })}}>{this.state.choosenCategory.name}</p>
                        :<p className={styles.choosenCategory} 
                            style={{color: '#cd851e'}} 
                            onClick={()=>{
                                this.setState({
                                    categoriesClass : (this.state.categoriesClass === styles.hidden)?styles.categories:styles.hidden
                                    })}}>Choose category</p>}
                        <div className={this.state.categoriesClass}>
                            {this.state.categories.map((category)=>{
                                return <p key={category.category_id} 
                                    className={styles.category}
                                    onClick={()=>{
                                        this.setState({
                                            choosenCategory : category,
                                            categoriesClass : (this.state.categoriesClass === styles.hidden)?styles.categories:styles.hidden
                                        })}}>{category.name}</p>})}
                        </div>
                    </div>
                    <Textarea className={this.state.errorClass} 
                    placeholder='Input description' 
                    label='Description' 
                    id='#description' 
                    onChange={(e)=>{this.setState({productDescription : e.target.value})}}/>    
                    <Textarea className={this.state.errorClass} 
                    placeholder='Input specifications' 
                    label='Specifications' 
                    id='#specifications'
                    onChange={(e)=>{this.setState({productSpecifications : e.target.value})}}/>
                    <div className={styles.imageBlock}>
                        <Input placeholder='Input image url' 
                        label='Image' 
                        className={this.state.errorClass}
                        onChange={(e)=>{this.setState({ productImage : e.target.value})}}/>
                        <img src={this.state.productImage} className={styles.img}></img>
                    </div>
                    <Button value='Create' onClick={this.createProduct} bgColor='#d58520'></Button>
                </div>
                :<Load/>}
            </div>
        )
    }
}
