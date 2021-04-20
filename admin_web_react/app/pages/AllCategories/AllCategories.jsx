import React, { Component } from 'react'
import axios from 'axios'

import styles from './style.css'
import Load from '../../components/Load/Load.jsx'
import Button from '../../components/Button/Button.jsx';
import {API_GETEWAY_HOST} from './../../app.jsx'

export default class AllCategories extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            categories : undefined  
        };

        this.deleteCategory = this.deleteCategory.bind(this);
        this.geyCategories = this.geyCategories.bind(this);
    }
    
    componentDidMount(){
        this.geyCategories();
    }
    
    geyCategories(){
        axios.get(API_GETEWAY_HOST+'categories', {withCredentials:true})
        .then((res)=>{
            this.setState({
                categories :res.data.categories
            });
        })
        .catch((er)=>{
            console.log(er);
        });
    }

    deleteCategory(id){
        axios.get(API_GETEWAY_HOST+'delete_category?id='+id, {withCredentials:true})
        .then(()=>{
            console.log('Category delete');
            this.geyCategories();
        })
        .catch((er)=>{
            console.log(er);
        });
    }

    render() {
        return (
            <div>
                {(this.state.categories)
                ?<div className={styles.allCategories}>
                    {this.state.categories.map((category)=>{
                        return <div key={category.category_id} className={styles.oneCategory}>
                                    <div className={styles.allTextlocks}>
                                        <div className={styles.textBlock}>
                                            <h3 className={styles.textTitle}>Category name:</h3>
                                            <p className={styles.textValue}>{category.name}</p>
                                        </div>
                                        <div className={styles.textBlock}>
                                            <h3 className={styles.textTitle}>Parent category:</h3>
                                            <p className={styles.textValue}>
                                                {(category.parent_name)
                                                ?category.parent_name
                                                :'None'}
                                            </p>
                                        </div>
                                        <div className={styles.textBlock}>
                                            <h3 className={styles.textTitle}>Final category:</h3>
                                            <p className={styles.textValue}>{(category.isNil)?'True':'False'}</p>
                                        </div>
                                    </div>
                                    <div className={styles.buttons}>
                                        <Button value='Edit' bgColor='#d58520' onClick={()=>{
                                            const { history } = this.props;
                                            history.push('/all_categories/'+category.category_id);}}/>
                                        <Button value='Delete' bgColor='#f44336' onClick={(e)=>{this.deleteCategory(category.category_id,e)}}/>
                                    </div>
                                </div>
                    })}
                </div>
                :<Load/>}
                
            </div>
        )
    }
}
