import React, { Component } from 'react'
import axios from 'axios'
import {API_HOST} from '../../app.jsx'

import Load from '../../components/Load/Load.jsx'
import styles from './style.css'
import { Link } from 'react-router-dom'

export default class Home extends Component {
    constructor(params) {
        super(params);

        this.state = {
            rootCategories : undefined
        } 
    }
    componentDidMount(){
        axios.get(API_HOST+'/root_categories',{withCredentials : true})
        .then((res)=>{
            console.log(res.data);
            this.setState({
                rootCategories : res.data.categories
            });
        })
        .catch((er)=>{
            console.log(er);
        })
    }

    render() {
        return (
            <div className={styles.home}>
                <h3 className={styles.h3}>Categories:</h3>
                {(this.state.rootCategories)
                ?<div className={styles.rootCategories}>
                    {this.state.rootCategories.map((category)=>{
                        return <Link to={'/category/'+category.category_id} key={category.category_id} className={styles.link}>{category.name}</Link>
                    })}
                </div>
                :<Load/>}
            </div>
        )
    }
}
