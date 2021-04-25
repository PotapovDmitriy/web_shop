import React, { Component } from 'react'
import axios from 'axios'

import styles from './style.css'
import Load from '../../components/Load/Load.jsx';
import Input from '../../components/Input/Input.jsx';
import Button from '../../components/Button/Button.jsx';
import {API_GETEWAY_HOST} from './../../app.jsx'

export default class RedactCategory extends Component {
    constructor(props) {
        super(props);
        
        this.state ={
            category : undefined,
            newCategoryName : undefined
        };

        this.saveCategoruChange = this.saveCategoruChange.bind(this);
    }

    componentDidMount(){
        axios.get(API_GETEWAY_HOST+'category?id=' + this.props.match.params.id, {withCredentials:true})
        .then((res)=>{
            this.setState({
                category : res.data,
                newCategoryName : res.data.name
            });
        })
        .catch((er)=>{
            console.log(er);
        });
    }
    
    saveCategoruChange(){
        if(this.state.newCategoryName !== ''){
            let data = {
                name : this.state.newCategoryName,
                category_id : this.props.match.params.id
            };
            axios.post(API_GETEWAY_HOST+'redact_category?id=' + this.props.match.params.id,data, {withCredentials:true})
            .then((res)=>{
                console.log('Category update');
                const { history } = this.props;
                history.push('/all_categories');
            })
            .catch((er)=>{
                console.log(er);
            });
        }
    }

    render() {
        return (
            <div>
                {(this.state.category)
                ?<div className={styles.redactCategory}>
                    <h2 className={styles.h2}>Redact category</h2>
                    <Input placeholder='Input category name' 
                        label='Category name' 
                        id='#category_name'
                        onChange={(e)=>{this.setState({ newCategoryName : e.target.value})}}
                        value={this.state.newCategoryName}
                        className={this.state.errorClass}/>
                    <div className={styles.categoryBlock}>
                        <p className={styles.categoryDescription}>Parent category</p>
                        <p className={styles.choosenCategory}>{(this.state.category.parent_name)?this.state.category.parent_name:'None'}</p>
                    </div>
                    <div className={styles.nillBlock}>
                        <p className={styles.nillDiscription}>Final category: </p>
                        <p className={styles.nillValue}>{(this.state.category.isNil)?'True':'False'}</p>
                    </div>
                    <Button value='Save' onClick={this.saveCategoruChange} bgColor='#d58520'></Button>
                </div>
                :<Load/>}
            </div>
        )
    }
}
